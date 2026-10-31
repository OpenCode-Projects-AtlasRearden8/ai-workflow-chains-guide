#!/usr/bin/env python3
"""Build the AI Workflow Chains Guide static site.

Reads the Markdown manual from docs/ and writes a dependency-free static
HTML site to site/. Local-first by design: no network calls, no tracking,
no JavaScript required to read the result.

Usage:
    python3 build.py            build site/ from docs/
    python3 build.py --check    build into a temp dir and exit (verification)
"""

import argparse
import posixpath
import re
import shutil
import sys
import tempfile
from pathlib import Path

try:
    import markdown as _markdown
except ImportError:  # pragma: no cover - surfaced with a friendly message
    _markdown = None

ROOT = Path(__file__).resolve().parent
DOCS_DIR = ROOT / "docs"
SITE_DIR = ROOT / "site"
ASSETS_SRC = ROOT / "assets" / "site.css"

SITE_TITLE = "AI Workflow Chains Guide"
SITE_TAGLINE = "A friendly manual for chaining AI steps into small everyday workflows."

# Reading order drives navigation, prev/next links, and index ordering.
PAGES = [
    ("docs/index.md", "Start here"),
    ("docs/01-break-the-job-into-steps.md", "1. Break the job into steps"),
    ("docs/02-feed-the-answer-forward.md", "2. Feed the answer forward"),
    ("docs/03-template-files-that-hold-your-chain.md", "3. Template files"),
    ("docs/04-switching-models-mid-chain.md", "4. Switching models mid-chain"),
    ("docs/05-debugging-bad-links.md", "5. Debugging bad links"),
    ("docs/06-saving-chains-you-reuse.md", "6. Saving chains you reuse"),
    ("docs/07-honest-limits.md", "7. Honest limits"),
    ("docs/worksheet.md", "The worksheet"),
    ("docs/glossary.md", "Glossary"),
    ("docs/chains/plan-a-trip.md", "Chain: plan-a-trip"),
    ("docs/chains/vet-a-purchase.md", "Chain: vet-a-purchase"),
    ("docs/chains/prep-a-meeting.md", "Chain: prep-a-meeting"),
]

_CSS = (ASSETS_SRC.read_text(encoding="utf-8") if ASSETS_SRC.exists() else "")


class BuildError(Exception):
    """Raised when the build cannot produce a complete site."""


def _to_html(md_path: Path) -> str:
    """Convert a Markdown file to HTML from an in-tree copy of site.css."""
    if _markdown is None:
        raise BuildError(
            "The Python package 'markdown' is required (see requirements.txt). "
            "Install locally once with: python3 -m pip install -r requirements.txt"
        )
    text = md_path.read_text(encoding="utf-8")
    return _markdown.markdown(
        text, extensions=["fenced_code", "tables", "sane_lists"]
    )


def _rel_src_to_site(src: Path | str) -> Path:
    """Map docs/foo.md to the site-relative path site/foo.html."""
    p = Path(src)
    if not p.is_absolute():
        p = (ROOT / p).resolve()
    rel = p.relative_to(DOCS_DIR).with_suffix(".html")
    return rel


def _rewrite_links(body: str, page_src: Path) -> str:
    """Rewrite internal .md links to known .html outputs; verify they resolve.

    External links (http/https/mailto) are left untouched. Any Markdown link
    that points at a doc path which is not one of the declared PAGES raises.
    """
    href_re = re.compile(r'href="([^"#]+)"')

    def repl(match: "re.Match[str]") -> str:
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:", "//")):
            return match.group(0)
        resolved = (page_src.parent / target).resolve()
        if not resolved.exists():
            raise BuildError(
                f"{page_src.relative_to(ROOT)}: link target does not exist: {target}"
            )
        if resolved.suffix == ".md":
            site_rel = _rel_src_to_site(resolved)
            # links must be relative to the page's own directory in the site
            href = posixpath.relpath(
                site_rel.as_posix(), _rel_src_to_site(page_src).parent.as_posix() or "."
            )
            return f'href="{href}"'
        # relative asset-style links (e.g. images) are copied verbatim
        return match.group(0)

    return href_re.sub(repl, body)


def _page_html(src_rel: str, title: str, html_body: str) -> str:
    """Wrap a page in the shared shell with nav and prev/next links."""
    site_rel = _rel_src_to_site(Path(src_rel))
    base = ("../" * len(site_rel.parent.parts)) if site_rel.parent != Path(".") else ""
    idx = PAGES.index((src_rel, title))
    prev_pair = PAGES[idx - 1] if idx > 0 else None
    next_pair = PAGES[idx + 1] if idx + 1 < len(PAGES) else None

    def _page_href(target_src: str) -> str:
        return posixpath.relpath(
            _rel_src_to_site(Path(target_src)).as_posix(),
            site_rel.parent.as_posix() or ".",
        )

    nav_items = []
    for p_src, p_title in PAGES:
        here = p_src == src_rel
        prefix = "&#9656; " if here else ""
        p_href = posixpath.relpath(
            _rel_src_to_site(Path(p_src)).as_posix(),
            site_rel.parent.as_posix() or ".",
        )
        nav_items.append(
            f'<li class="{"here" if here else ""}">'
            f'<a href="{p_href}">{prefix}{p_title}</a></li>'
        )
    nav = "\n".join(nav_items)

    crumbs = []
    if site_rel.parent != Path("."):
        crumbs.append(
            f'<a href="{"../" * len(site_rel.parent.parts)}index.html">{SITE_TITLE}</a>'
        )
        crumbs.append(site_rel.stem)
    else:
        crumbs.append(SITE_TITLE)
    breadcrumb = " &rsaquo; ".join(crumbs)

    prev_next = ""
    links = []
    if prev_pair:
        links.append(
            f'<a class="pn prev" href="{_page_href(prev_pair[0])}">'
            f"&larr; {prev_pair[1]}</a>"
        )
    if next_pair:
        links.append(
            f'<a class="pn next" href="{_page_href(next_pair[0])}">'
            f"{next_pair[1]} &rarr;</a>"
        )
    if links:
        prev_next = '<div class="prevnext">' + "".join(links) + "</div>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} &middot; {SITE_TITLE}</title>
<meta name="description" content="{SITE_TAGLINE}">
<style>{_CSS}</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <div class="brand">
      <a href="{posixpath.relpath('index.html', site_rel.parent.as_posix() or '.')}">{SITE_TITLE}</a>
    </div>
    <p class="tagline">{SITE_TAGLINE}</p>
    <nav>
      <ul class="navlist">
{nav}
      </ul>
    </nav>
    <p class="sidebar-note">Local-first &middot; no tracking &middot; MIT, &copy; 2026 Asdale Dynamics, LLC</p>
  </aside>
  <main class="content">
    <p class="breadcrumb">{breadcrumb}</p>
{html_body}
{prev_next}
  </main>
</div>
</body>
</html>
"""


def build(out_dir: Path) -> list:
    """Build the full site into out_dir. Returns list of written pages."""
    if not DOCS_DIR.is_dir():
        raise BuildError(f"docs/ directory not found at {DOCS_DIR}")

    written = []
    for src_rel in {src for src, _ in PAGES}:
        src = ROOT / src_rel
        if not src.exists():
            raise BuildError(f"declared page missing: {src_rel}")
        title = dict(PAGES)[src_rel]
        body = _rewrite_links(_to_html(src), src)
        html = _page_html(src_rel, title, body)
        dest = out_dir / _rel_src_to_site(src)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")
        written.append(dest)

    return written


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build the static site.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="build into a temporary directory instead of site/ (verification only)",
    )
    args = parser.parse_args(argv)

    target = SITE_DIR
    try:
        if args.check:
            with tempfile.TemporaryDirectory(prefix="chains-site-") as tmp:
                wrote = build(Path(tmp))
            print(f"OK: built and verified {len(wrote)} pages (no output written).")
        else:
            if target.exists():
                shutil.rmtree(target)
            target.mkdir(parents=True, exist_ok=True)
            wrote = build(target)
            print(f"OK: built {len(wrote)} pages into {target.relative_to(ROOT)}/")
    except BuildError as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
