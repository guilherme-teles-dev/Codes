import pymupdf4llm

md_text = pymupdf4llm.to_markdown("2016_the-linux-command-line_a-complete-introduction.pdf")

import pathlib

pathlib.Path("2016_the-linux-command-line_a-complete-introduction.md").write_bytes(md_text.encode())