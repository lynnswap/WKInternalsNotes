# WKInternalsNotes

Notes on WebKit UIProcess Objective-C APIs and internal behaviors, maintained as
DocC documentation extensions and synthetic symbol graphs.

## Scope
- Cocoa APIs under `Source/WebKit/UIProcess`
- Internal APIs and observed behaviors

## Baseline revision
- The reference WebKit revision is pinned in `WebKit.revision`.
- Reference links are tied to that revision.

## Repository layout
- `Sources/WKInternalsNotes/Documentation.docc`: main DocC content
- `Scripts`: generation and sync helpers
- `WebKit.revision`: pinned WebKit revision
- `References/WebKit`: local WebKit checkout
- `Developers.md`: developer notes (symbol graph generation, scripts)

## For developers
- See [`Developers.md`](Developers.md) for developer workflows.

## Notes
- Each entry records behavior, defaults, and the WebKit source paths it refers to.
- The content is updated as research progresses and may change over time.
- This content is research notes and is provided without guarantees of accuracy or completeness; use at your own risk.

## Licensing and attribution
- WebKit is licensed under its own terms; see [WebKit](https://github.com/WebKit/WebKit).
