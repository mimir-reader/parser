# parser


### v0.1 --> pymupdf4llm -- doesnt work well

### v0.2 --> docling -- better. issues with extracting formulae and images

Latex Spacing Issue: https://github.com/docling-project/docling/issues/2374 -- **unsolved**

Unknown text in images: https://github.com/docling-project/docling/discussions/2506 -- use `PyPdfiumDocumentBackend` backend

### v0.2.1 --> docling image ocr issue fix

This version just fixes the text artifact issue in extracted images by utilizing the `PyPdfiumDocumentBackend` backend.

`DoclingParseDocumentBackend` better than `PyPdfiumBackend` for text. we can just extract images from the coords given in `manifest.json`. 

formula quality is bad anyways so it doesnt matter. but `PyPdfiumBackend` mess up tables so that's more of a reason to use the default on.






plan: for a basic version ill use pdf.js or maybe some other alternate library which would JUST show the hyperlinked or mentioned elements in sidebar.
