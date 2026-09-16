import pymupdf4llm
from pathlib import Path

import json

# markdown
"""
# Extract Markdown with images saved to disk
md_text = pymupdf4llm.to_markdown(
    "1706.03762v7.pdf",
    write_images=True,
    image_path="output_md/images/",
    image_format="png",
    dpi=150
)

# Save the Markdown file
Path("output_md/report.md").write_text(md_text, encoding="utf-8")

print("Done.")
print(f"Images saved to: output/images/")
print(f"Markdown saved to: output/report.md")
"""


# JSON
"""
# parse the file 
json_str = pymupdf4llm.to_json("1706.03762v7.pdf")

# Convert JSON to Python Dictionary and iterate through the content
data = json.loads(json_str)

def parse_span_flags(flags: int):
    return {
        "superscript": bool(flags & 1),
        "italic": bool(flags & 2),
        "serifed": bool(flags & 4),
        "monospaced": bool(flags & 8),
        "bold": bool(flags & 16),
    }

# iterate through the document
output_data = []
for page_num, page in enumerate(data.get("pages", [])):
    print(f"\nPage {page_num}")

    for block in page.get("boxes", []):
        for line in (block.get("textlines") or []):
            for span in line.get("spans", []):
                text = span.get("text", "")
                flags = span.get("flags", 0)
                styles = parse_span_flags(flags)

                print({
                    "text": text,
                    "flags": flags,
                    "styles": styles
                })
                output_data.append(
                    {
                        "text": text,
                        "flags": flags,
                        "styles": styles
                    }
                )

with open('output_json/output.jsonl', 'w') as f:
    for item in output_data:
        f.write(json.dumps(item) + '\n')
"""