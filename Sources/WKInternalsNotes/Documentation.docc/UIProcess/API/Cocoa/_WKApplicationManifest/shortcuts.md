# ``WKInternalsNotes/_WKApplicationManifest/shortcuts``

ショートカット一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<_WKApplicationManifestShortcut *> *shortcuts WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Discussion
`ApplicationManifest` のショートカット配列を `_WKApplicationManifestShortcut` の配列として生成して返す。

## References
- [`_WKApplicationManifest.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L88)
- [`_WKApplicationManifest.mm#L491`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L491)
- [`_WKApplicationManifest.mm#L493`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L493)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
