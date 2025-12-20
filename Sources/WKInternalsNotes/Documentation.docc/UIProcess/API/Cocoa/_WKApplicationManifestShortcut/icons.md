# ``WKInternalsNotes/_WKApplicationManifestShortcut/icons``

ショートカットのアイコン配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<_WKApplicationManifestIcon *> *icons;
```

## Discussion
`initWithCoreShortcut:` で `shortcut->icons` を `_WKApplicationManifestIcon` 配列に変換して保持し、そのまま返す。

## References
- [`_WKApplicationManifest.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L121)
- [`_WKApplicationManifest.mm#L204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L204)
- [`_WKApplicationManifest.mm#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L217)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
