# GIACONVERT — Word to HTML

A personal, AI-assisted document-conversion project for people preparing Word content for the web. Python CLI tools and a local FastAPI/Vue interface offer text/table, image, and header/footer workflows.

## Portfolio context

My focus is the document workflow: requirements, output choices, error messages, documentation, and validation. Implementation is AI-assisted. This is a personal project, separate from employer work; no measured productivity or production-adoption claim is made.

Start with the [workflow case study](Documentation/PORTFOLIO_CASE_STUDY.md), [GUI requirements](Documentation/GUI_REQUIREMENTS.md), and [error taxonomy](Documentation/ERROR_TAXONOMY.md). Requirements and plans describe intended behavior; they are not proof that every option is implemented.

## Quick start

Use Python 3.9+ as the onboarding baseline. Earlier Python versions are not validated here. Run from the repository root:

```bash
git clone https://github.com/giarcheuli/GIACONVERT.git
cd GIACONVERT
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python launch.py
```

The launcher expects `.venv/bin/python`, starts the local server, and opens a browser. `setup.sh` is an older CLI setup script; it does not create the environment required by the launcher.

For a small CLI dependency set:

```bash
python -m pip install python-docx==0.8.11 lxml==4.9.3 click==8.1.7 Pillow==10.4.0
python giaconvert.py /path/to/a/copied-docx-folder
```

## Choose a workflow

| Entry point | Purpose |
|---|---|
| `giaconvert.py` | DOCX text and tables |
| `giaconvert_with_images.py` | DOCX with external, inline, or skipped images |
| `giaconvert_complete.py` | DOCX with image and header/footer options |
| `giaconvert_universal.py` / `app.py` | Universal conversion used by the local web interface |

```bash
python giaconvert_complete.py /path/to/copied-documents --images external --headers-footers include
python giaconvert_complete.py /path/to/copied-documents --images inline --headers-footers print-only
```

HTML is written beside source documents by the CLI; external images use a companion folder. Use copies and a fresh output location when evaluating, because existing HTML may be overwritten.

## Examples and verification

The [synthetic example](examples/README.md) includes reproducible source and generated HTML. It contains no employer or client material.

```bash
python examples/create_sample.py
python Tests/test_converters.py
```

The smoke script checks all three DOCX converter modules, sample text and table content, and returns a nonzero status on failure. It does not establish browser compatibility, visual fidelity, image/header coverage, or legacy DOC reliability.

## Decisions and documentation

- [Output/storage strategy](Documentation/STORAGE_STRATEGY.md): output placement and workflow choices.
- [Error taxonomy](Documentation/ERROR_TAXONOMY.md): errors and recovery wording; design reference, not a verified implementation checklist.
- [Quick reference](Documentation/QUICK_START.md) and [web implementation notes](Documentation/WEB_APP_COMPLETE.md): supplementary guides; use the setup above as the current entry point.

## Limitations and status

Local prototype with multiple converter implementations. The web app uses the universal converter, so CLI smoke results do not prove web-mode parity. DOCX is the demonstrated path. Legacy binary `.doc` handling, complex layouts, image fidelity, and full web flows need separate acceptance testing. No hosted service is provided.

## License

The existing usage statement is retained: provided as-is for personal and educational use. No broader license is granted by this README.
