# Synthetic DOCX → HTML example

Run `python examples/create_sample.py` from the repository root after installing the small CLI dependency set in the README. The script creates `sample.docx`, converts it with the basic converter into `sample.html`, and asserts preservation of the heading text, table row, and bold markup. No AI service or API token is used.

Open [sample.html](sample.html) in a browser to inspect the generated output. The input is fictional and created entirely by [create_sample.py](create_sample.py); no employer or client material is included. The binary DOCX is generated locally rather than tracked; regenerate it to compare input and output.

This demonstrates one basic DOCX workflow. It does not validate images, page layout, legacy DOC input, the web app, or every documented requirement.
