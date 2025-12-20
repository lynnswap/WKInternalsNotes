# ``WKInternalsNotes/_WKApplicationManifest/icons``

アイコン一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<_WKApplicationManifestIcon *> *icons WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`ApplicationManifest` のアイコン配列を `_WKApplicationManifestIcon` の配列として生成して返す。

## References
- [`_WKApplicationManifest.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L87)
- [`_WKApplicationManifest.mm#L484`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L484)
- [`_WKApplicationManifest.mm#L486`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L486)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
