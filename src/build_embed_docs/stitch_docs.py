import pathlib
import re  # <-- new

ROOT = pathlib.Path(__file__).resolve().parent
DOCS_DIR = ROOT / "manim_docs"
OUTPUT_FILE = ROOT / "unified_manim_community_docs.md"
OUTPUT_FILE2 = ROOT / "unified_manim_community_docs2.md"
OUTPUT_FILE3 = ROOT / "unified_manim_community_docs3.md"


def clean_content(text: str) -> str:
    """Strip boilerplate headers from a single page."""

    # Drop everything up to (and including) the toggle prompt if present.
    toggle_marker = "Toggle table of contents sidebar"
    if toggle_marker in text:
        after_toggle = text.split(toggle_marker, 1)[1]
        # Remove the toggle line itself (assume it ends at the next newline)
        text = after_toggle.lstrip("\n")

    # Remove the language/version banner block if present.
    lang_marker = "Languages**[en]"
    divider = "* * *"
    if lang_marker in text:
        start = text.index(lang_marker)
        # Cut through the first divider after the block (typically '* * *').
        end = text.find(divider, start)
        if end != -1:
            end += len(divider)
            text = text[:start].rstrip("\n") + "\n" + text[end:].lstrip("\n")

    return text.strip() + "\n"


def strip_front_matter(text: str) -> str:
    """Remove YAML front matter entirely (discard url/title)."""

    if not text.startswith("---"):
        return text

    end = text.find("\n---", 3)
    if end == -1:
        return text

    remainder = text[end + 4 :].lstrip("\n")
    return remainder


def normalize_fence_backslashes(text: str) -> str:
    """Turn lines like ```\\ into proper ``` so fences are detected correctly."""

    # Match lines that start with fences (``` or more backticks) and end with a backslash.
    # Example: ```\  ->  ```
    return re.sub(
        r'^([ \t]*```+)\s*\\\s*$',
        r'\1',
        text,
        flags=re.MULTILINE,
    )


def transform_headings_and_code(text: str, bump: int = 1) -> str:
    """Demote headings outside fenced code; escape # inside fences."""

    lines = text.splitlines()
    out = []
    in_fence = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue

        if in_fence:
            out.append(line)
            continue

        if stripped.startswith("#"):
            hashes, rest = stripped.split(maxsplit=1) if " " in stripped else (stripped, "")
            new_hashes = "#" * (len(hashes) + bump)
            new_line = " " * (len(line) - len(stripped)) + new_hashes
            if rest:
                new_line += f" {rest}"
            out.append(new_line)
        else:
            out.append(line)

    return "\n".join(out)


def ensure_balanced_fences(text: str) -> str:
    """Ensure fenced code blocks are closed so following headings are not swallowed."""

    fence_count = text.count("```")
    if fence_count % 2 == 1:
        # Append a closing fence without touching existing fence lines.
        return text.rstrip("\n") + "\n```"
    return text


def main() -> None:
    if not DOCS_DIR.is_dir():
        raise SystemExit(f"Docs directory not found: {DOCS_DIR}")

    pieces = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        content = path.read_text(encoding="utf-8", errors="ignore")
        body = strip_front_matter(content)
        cleaned = clean_content(body)
        cleaned = cleaned.replace(
            "Toggle Light / Dark / Auto color theme", ""
        ).replace("Toggle table of contents sidebar", "")
        cleaned_lines = [
            line
            for line in cleaned.splitlines()
            if not line.startswith("[Back to top](")
            and "Addons documentation" not in line
            and "Read the Docs" not in line
        ]
        cleaned = "\n".join(cleaned_lines).strip() + "\n"

        # *** Fix for ```\ -> ``` so fences are seen correctly ***
        cleaned = normalize_fence_backslashes(cleaned)

        rel = path.relative_to(ROOT)
        rel_str = rel.as_posix()

        # Apply heading/code transforms after boilerplate removal and fence fix.
        cleaned = transform_headings_and_code(cleaned)
        cleaned = ensure_balanced_fences(cleaned)

        # Use file name as top heading.
        top_heading = f"# {rel_str}\n\n"
        # Use explicit comments to mark doc boundaries for downstream splitting.
        header = f"<!-- DOC START: {rel_str} -->\n# {rel_str}\n\n"
        footer = "\n<!-- DOC END -->"
        # Drop the noisy header for the long reference files.
        if rel_str.startswith("manim_docs/docs.manim.community_en_stable_referen"):
            header = ""
            footer = ""
        pieces.append(f"{header}{top_heading}{cleaned}{footer}")

    # Use explicit doc boundary markers that are not affected by markdown hierarchy.
    stitched = "\n\n".join(pieces)
    OUTPUT_FILE.write_text(stitched, encoding="utf-8")
    OUTPUT_FILE2.write_text(stitched, encoding="utf-8")
    OUTPUT_FILE3.write_text(stitched, encoding="utf-8")
    print(
        f"Wrote {OUTPUT_FILE}, {OUTPUT_FILE2}, and {OUTPUT_FILE3} with {len(pieces)} documents."
    )


if __name__ == "__main__":
    main()
