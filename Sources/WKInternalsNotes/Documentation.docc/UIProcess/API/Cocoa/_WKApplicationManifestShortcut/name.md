# ``WKInternalsNotes/_WKApplicationManifestShortcut/name``

ショートカット名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *name;
```

## Discussion
`initWithCoreShortcut:` で `shortcut->name` を `NSString` に変換して保持し、そのまま返す。

## References
- [`_WKApplicationManifest.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L119)
- [`_WKApplicationManifest.mm#L194`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L194)
- [`_WKApplicationManifest.mm#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L214)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
