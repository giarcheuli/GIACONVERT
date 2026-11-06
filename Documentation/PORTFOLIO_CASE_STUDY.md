# Case study: a document-publishing workflow

## Problem and contribution

A Word document needs to become web content. A non-technical user needs to choose files, understand output placement, select image handling, and recover from conversion failures.

This personal project uses AI-assisted implementation. My focus is requirements, documentation, workflow choices, acceptance criteria, and validation. The repository is evidence of the artifacts and implementation, not an employer deliverable or a measured productivity claim.

## Decisions and evidence

| Question | Artifact and rationale |
|---|---|
| Who is the interface for? | [GUI requirements](GUI_REQUIREMENTS.md) define business users, content creators, and batch workflows. This is a design document with proposals, not a verified feature checklist. |
| Where should output go? | [Storage strategy](STORAGE_STRATEGY.md) describes output choices. CLI examples start with copies so evaluation does not overwrite valuable HTML. |
| How are images delivered? | [Image plan](IMAGE_SUPPORT_PLAN.md) and converter options distinguish portable inline content from separate image assets. |
| How does a failed conversion help the user recover? | [Error taxonomy](ERROR_TAXONOMY.md) pairs failures with understandable messages and suggested actions; runtime coverage still needs acceptance testing. |
| What is a dependable first verification? | [Converter smoke script](../Tests/test_converters.py) locates modules at the repository root, checks preserved text/table content, and fails the process when a converter fails. |

## Demonstration

The [synthetic example](../examples/README.md) generates a fictional DOCX request and real HTML using the basic converter. Its assertions check heading text, a table row, and bold markup. The generated HTML is included for inspection; it is not a hand-written mockup.

The separate smoke script exercises basic, image-capable, and complete modules on a text/table fixture. It does not test image extraction or headers merely because those modules are loaded.

## Status and limits

The demonstrated path is local DOCX conversion. The web application uses a separate universal converter; parity between web modes and the CLI modules is unverified. Binary DOC support and complex visual fidelity require dedicated fixtures and acceptance runs. No adoption, throughput, or time-saving outcome is claimed.

Next slice: map a small selection of error-taxonomy cases to actual API responses, then add dated UAT evidence for a failed file, a successful file, and output placement. This is proposed follow-up work.

[Repository entry point](../README.md)
