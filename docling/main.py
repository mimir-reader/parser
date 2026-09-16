from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend

import json

output_dir = Path("output")
image_dir = output_dir / "images"
image_dir.mkdir(parents=True, exist_ok=True)

pdf_pipeline_options = PdfPipelineOptions(
    do_ocr = False,
    do_table_structure = True,
    generate_picture_images = True,
    images_scale = 2.0,
    do_formula_enrichment = True
)

converter = DocumentConverter(
    format_options = {
        InputFormat.PDF: PdfFormatOption(
            pipeline_options=pdf_pipeline_options,
            backend=PyPdfiumDocumentBackend
        )
    }
)

result = converter.convert("1706.03762v7.pdf")
doc = result.document

markdown = doc.export_to_markdown()
(output_dir/"report_md.md").write_text(markdown, encoding="utf-8")

doc_dict = json.dumps(doc.export_to_dict(), indent=2, ensure_ascii=False)
(output_dir/"report_json.json").write_text(doc_dict, encoding="utf-8")

manifest = []
for item, _level in doc.iterate_items():
    if item.label.name in ("PICTURE", "TABLE"):
        img = item.get_image(doc)
        if img is None:
            continue
        page_no = item.prov[0].page_no if item.prov else 0
        fname = f"{item.label}_p{page_no}_{len(manifest)}.png"
        img.save(image_dir / fname)
        manifest.append({
            "id": len(manifest),
            "label": item.label,
            "page": page_no,
            "file": fname,
            "bbox": item.prov[0].bbox.as_tuple() if item.prov else None,
        })

import json
(output_dir/"manifest.json").write_text(json.dumps(manifest, indent=2))

print(f"Done. {len(manifest)} figures/tables saved to {image_dir}/")
print(f"Markdown: {output_dir/'report_md.md'}")
print(f"JSON: {output_dir/'report_json.json'}")