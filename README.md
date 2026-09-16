# parser


### v0.1 --> pymupdf4llm -- doesnt work well

### v0.2 --> docling -- better. issues with extracting formulae and images

Latex Spacing Issue: https://github.com/docling-project/docling/issues/2374 -- **unsolved**

Unknown text in images: https://github.com/docling-project/docling/discussions/2506 -- use `PyPdfiumDocumentBackend` backend

### v0.2.1 --> docling image ocr issue fix

This version just fixes the text artifact issue in extracted images by utilizing the `PyPdfiumDocumentBackend` backend.
