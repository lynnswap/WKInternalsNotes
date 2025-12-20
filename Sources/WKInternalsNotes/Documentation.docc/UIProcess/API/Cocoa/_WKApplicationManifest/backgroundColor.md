# ``WKInternalsNotes/_WKApplicationManifest/backgroundColor``

背景色を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) UIColor *backgroundColor WK_API_AVAILABLE(ios(17.0));
```

## Discussion
`ApplicationManifest` の `backgroundColor` を Cocoa の色に変換して返す。

## References
- [`_WKApplicationManifest.h#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L91)
- [`_WKApplicationManifest.mm#L423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
