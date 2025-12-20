# ``WKInternalsNotes/_WKApplicationManifest/categories``

カテゴリ一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSString *> *categories WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Discussion
`ApplicationManifest` のカテゴリ配列を `NSArray<NSString *>` に変換して返す。

## References
- [`_WKApplicationManifest.h#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L86)
- [`_WKApplicationManifest.mm#L477`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L477)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
