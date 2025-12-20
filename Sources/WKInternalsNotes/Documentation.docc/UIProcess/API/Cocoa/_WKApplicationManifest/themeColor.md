# ``WKInternalsNotes/_WKApplicationManifest/themeColor``

テーマカラーを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) UIColor *themeColor WK_API_AVAILABLE(ios(15.0));
```

## Discussion
`ApplicationManifest` の `themeColor` を Cocoa の色に変換して返す。

## References
- [`_WKApplicationManifest.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L97)
- [`_WKApplicationManifest.mm#L428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
