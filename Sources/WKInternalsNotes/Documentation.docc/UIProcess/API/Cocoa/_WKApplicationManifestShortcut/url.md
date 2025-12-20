# ``WKInternalsNotes/_WKApplicationManifestShortcut/url``

ショートカット URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURL *url;
```

## Discussion
`initWithCoreShortcut:` で `shortcut->url` を `NSURL` に変換して保持し、そのまま返す。

## References
- [`_WKApplicationManifest.h#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L120)
- [`_WKApplicationManifest.mm#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L199)
- [`_WKApplicationManifest.mm#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
