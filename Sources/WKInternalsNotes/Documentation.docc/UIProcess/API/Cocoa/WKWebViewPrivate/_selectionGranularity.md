# ``WKInternalsNotes/WKWebView/_selectionGranularity``

`_selectionGranularity` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKSelectionGranularity _selectionGranularity WK_API_DEPRECATED("This property is ignored; selection granularity is always `character`.", ios(8.0, 11.0), visionos(1.0, 1.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/ios/WKWebViewIOS.h#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L199)
- [`API/ios/WKWebViewIOS.mm#L549`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L549)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
