# ``WKInternalsNotes/WKWebView/_createPDFPageNumberIndicator(_:withFrame:pageCount:)``

`_createPDFPageNumberIndicator` を実行する。

## Objective-C Declaration
```objective-c
- (void)_createPDFPageNumberIndicator:(WebKit::PDFPluginIdentifier)identifier withFrame:(CGRect)rect pageCount:(size_t)pageCount;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L620`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L620)
- [`WKWebView.mm#L3101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
