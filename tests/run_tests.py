#!/usr/bin/env python3
"""Test suite for the AI Workflow Chains Guide.

Runs with the standard library only:  python3 tests/run_tests.py

Covers:
  1. Structural tests   - every manual page exists, well-formed, complete
  2. Content tests      - the goal's required topics are genuinely covered
  3. Link tests         - every internal Markdown link resolves
  4. Build tests        - the site builds into a temp dir with valid HTML
  5. Privacy tests      - no secrets / keys / personal-data patterns
"""

import html.parser
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build as build_mod  # noqa: E402

DOCS = ROOT / "docs"

EXPECTED_PAGES = [
    "docs/index.md",
    "docs/01-break-the-job-into-steps.md",
    "docs/02-feed-the-answer-forward.md",
    "docs/03-template-files-that-hold-your-chain.md",
    "docs/04-switching-models-mid-chain.md",
    "docs/05-debugging-bad-links.md",
    "docs/06-saving-chains-you-reuse.md",
    "docs/07-honest-limits.md",
    "docs/worksheet.md",
    "docs/glossary.md",
    "docs/chains/plan-a-trip.md",
    "docs/chains/vet-a-purchase.md",
    "docs/chains/prep-a-meeting.md",
]

# Phrases that must exist somewhere in a page for it to count as covering
# its goal-mandated topic (checking substance, not just an H1 title).
TOPIC_REQUIREMENTS = [
    ("docs/index.md", ["prompt-pattern-cookbook", "strings of prompts"]),
    ("docs/01-break-the-job-into-steps.md", ["thirty seconds", "brain-dump"]),
    ("docs/02-feed-the-answer-forward.md", ["[paste step 1's answer]", "using only these facts"]),
    ("docs/03-template-files-that-hold-your-chain.md", ["CHECK:", "WATCH OUT FOR"]),
    ("docs/04-switching-models-mid-chain.md", ["condensing", "local"]),
    ("docs/05-debugging-bad-links.md", ["reverse walk", "unframed paste"]),
    ("docs/06-saving-chains-you-reuse.md", ["plan-a-trip", "vet-a-purchase", "prep-a-meeting"]),
    ("docs/07-honest-limits.md", ["fact-checker", "privacy", "not a fact-checker"]),
    ("docs/worksheet.md", ["CHECK ", "one-breath"]),
    ("docs/glossary.md", ["Seam", "Paste", "Upstream"]),
]


def _all_pages() -> list:
    pages = []
    for rel in build_mod.PAGES:
        pages.append(ROOT / rel[0])
    return pages


def _md_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class PageStructureTests(unittest.TestCase):
    """Every declared page exists and follows the manual's shape."""

    def test_declared_pages_exist(self):
        for rel, _ in build_mod.PAGES:
            self.assertTrue((ROOT / rel).exists(), f"missing page: {rel}")

    def test_existing_clone_doc_pages_are_declared(self):
        for md in DOCS.rglob("*.md"):
            rel = md.relative_to(ROOT).as_posix()
            self.assertIn(rel, [r for r, _ in build_mod.PAGES],
                          f"undocumented page not in build manifest: {rel}")

    def test_every_page_has_h1(self):
        for p in _all_pages():
            self.assertTrue(
                re.search(r"^# .+", _md_text(p), re.M), f"no H1 in {p.name}"
            )

    def test_every_page_has_next_or_end(self):
        last_page = build_mod.PAGES[-1][0]
        for p in _all_pages():
            text = _md_text(p)
            last = [ln for ln in text.splitlines() if ln.strip()][-1]
            if p.relative_to(ROOT).as_posix() == last_page:
                continue  # the final page is allowed to end the trail
            has_next = last.startswith("[Next:") or "→]" in last
            self.assertTrue(has_next, f"{p.name} has no forward link at end")

    def test_glossary_covers_core_terms(self):
        text = _md_text(DOCS / "glossary.md").lower()
        for term in ["chain", "seam", "paste", "upstream", "downstream",
                     "condensing step", "blank", "drift"]:
            self.assertIn(term, text, f"glossary missing term: {term}")

    def test_glossary_alphabetical(self):
        text = _md_text(DOCS / "glossary.md")
        terms = re.findall(r"^\*\*(.+?)\*\*", text, re.M)
        sorted_terms = sorted(terms, key=str.lower)
        self.assertEqual(terms, sorted_terms, "glossary terms out of order")


class GoalCoverageTests(unittest.TestCase):
    """The manual covers every topic in the project's original goal."""

    def test_required_topics_are_substantively_covered(self):
        for rel, phrases in TOPIC_REQUIREMENTS:
            text = _md_text(ROOT / rel).lower()
            for phrase in phrases:
                self.assertIn(phrase.lower(), text,
                              f"{rel} missing required topic phrase: {phrase!r}")

    def test_three_worked_chains_use_house_template_sections(self):
        for name in ["plan-a-trip.md", "vet-a-purchase.md", "prep-a-meeting.md"]:
            text = _md_text(DOCS / "chains" / name)
            for section in ["CHAIN NAME:", "STEP 1", "CHECK:", "WATCH OUT FOR"]:
                self.assertIn(section, text, f"{name} missing section: {section}")

    def test_chains_reference_seam_steering_not_blind_following(self):
        for name in ["plan-a-trip.md", "vet-a-purchase.md", "prep-a-meeting.md"]:
            text = _md_text(DOCS / "chains" / name)
            self.assertIn("PASTE INTO", text,
                          f"{name} doesn't say where answers flow next")

    def test_worksheet_is_fillable(self):
        text = _md_text(DOCS / "worksheet.md")
        self.assertGreaterEqual(text.count("____"), 10,
                                "worksheet lacks fill-in blanks")


class LinkTests(unittest.TestCase):
    """Every internal Markdown link must point at a real file."""

    _LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    def test_all_internal_md_links_resolve(self):
        for p in _all_pages():
            text = _md_text(p)
            for target in self._LINK.findall(text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                resolved = (p.parent / target).resolve()
                self.assertTrue(
                    resolved.exists(),
                    f"{p.relative_to(ROOT)}: broken link to {target}"
                )


class _HTMLTextSkeleton(html.parser.HTMLParser):
    """Minimal validator: collects tags and text from built pages."""

    VOID_TAGS = {"meta", "br", "hr", "img", "link", "input", "source",
                 "base", "col", "embed", "track", "wbr", "area"}

    def __init__(self):
        super().__init__()
        self.stack = []
        self.text = []
        self.links_hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID_TAGS:
            self.stack.append(tag)
        if tag == "a":
            self.links_hrefs.append(dict(attrs).get("href", ""))

    def handle_startendtag(self, tag, attrs):
        if tag == "a":
            self.links_hrefs.append(dict(attrs).get("href", ""))

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, data):
        self.text.append(data)


class BuildTests(unittest.TestCase):
    """The build script produces a complete, valid static site."""

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory(prefix="chains-tests-")
        cls.out = Path(cls._tmp.name) / "site"
        cls.written = build_mod.build(cls.out)
        cls.built = {p.name: p for p in cls.written}

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_builds_one_page_per_manual_chapter(self):
        self.assertEqual(len(self.built), len(EXPECTED_PAGES))
        for rel in EXPECTED_PAGES:
            expected = build_mod._rel_src_to_site(ROOT / rel)
            self.assertIn((self.out / expected).read_text(encoding="utf-8"),
                          self.out.joinpath(expected).read_text(encoding="utf-8"))

    def test_every_built_page_is_balanced_html_with_content(self):
        for path in self.out.rglob("*.html"):
            text = path.read_text(encoding="utf-8")
            parser = _HTMLTextSkeleton()
            parser.feed(text)
            self.assertEqual(parser.stack, [],
                             f"{path.name}: unbalanced tags: {parser.stack}")
            joined = " ".join(" ".join(parser.text).split())
            self.assertGreater(len(joined), 200, f"{path.name}: too little text")

    def test_nav_links_on_every_page_resolve_to_built_files(self):
        for path in self.out.rglob("*.html"):
            text = path.read_text(encoding="utf-8")
            parser = _HTMLTextSkeleton()
            parser.feed(text)
            for href in parser.links_hrefs:
                if href.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = (path.parent / href).resolve()
                self.assertTrue(target.exists(),
                                f"{path.name}: nav link to missing {href}")

    def test_index_html_is_at_site_root(self):
        index = self.out / "index.html"
        self.assertTrue(index.exists())
        text = index.read_text(encoding="utf-8")
        self.assertIn("AI Workflow Chains Guide", text)
        self.assertIn("Asdale Dynamics", text)

    def test_index_links_to_all_three_chains(self):
        text = (self.out / "index.html").read_text(encoding="utf-8")
        for chain in ["plan-a-trip", "vet-a-purchase", "prep-a-meeting"]:
            self.assertIn(f"chains/{chain}.html", text)

    def test_build_check_mode_succeeds(self):
        # verify --check works end to end without writing to site/
        rc = build_mod.main(["--check"])
        self.assertEqual(rc, 0)


class PrivacyTests(unittest.TestCase):
    """No secrets, API keys, or personal-data patterns anywhere in-tree."""

    SECRET_PATTERN = re.compile(
        r"(?:"
        r"sk-[A-Za-z0-9]{16,}"            # OpenAI-style key
        r"|ghp_[A-Za-z0-9]{16,}"          # GitHub PAT
        r"|AKIA[0-9A-Z]{16}"              # AWS access key id
        r"|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|net|org)\b"  # emails
        r"|\b(?:\d{3})-?\d{2}-?\d{4}\b"   # US SSN
        r"|\b\d{1,3}(?:\.\d{1,3}){3}\b"   # IPv4 (should not appear; local docs)
        r")"
    )

    def _candidate_files(self):
        skip_dirs = {".git", "site", "__pycache__", ".pytest_cache"}
        for p in ROOT.rglob("*"):
            if p.is_dir() or any(part in skip_dirs for part in p.parts):
                continue
            if p.suffix.lower() in {".md", ".py", ".css", ".txt", ".html"}:
                yield p

    def test_no_secret_or_personal_data_patterns(self):
        offenders = []
        for p in self._candidate_files():
            text = p.read_text(encoding="utf-8", errors="ignore")
            for m in self.SECRET_PATTERN.finditer(text):
                offenders.append(f"{p.relative_to(ROOT)}: {m.group(0)[:24]}…")
        self.assertEqual([], offenders)

    def test_no_build_secrets_config(self):
        self.assertFalse((ROOT / ".env").exists())
        for name in ["config.json", "secrets", "credentials"]:
            self.assertFalse((ROOT / name).exists())


class READMEAndLicenseTests(unittest.TestCase):
    """Project-facing files carry required credits and instructions."""

    def test_license_exact_copyright_line(self):
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", text)
        self.assertIn("MIT License", text)

    def test_readme_credits_llc(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", text)
        self.assertIn("python3 build.py", text)
        self.assertIn("tests/run_tests.py", text)
        self.assertIn("prompt-pattern-cookbook", text)

    def test_readme_links_to_key_pages(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for target in ["docs/index.md", "docs/worksheet.md", "docs/glossary.md",
                       "docs/chains/plan-a-trip.md", "LICENSE"]:
            self.assertIn(target, text, f"README missing link to {target}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
