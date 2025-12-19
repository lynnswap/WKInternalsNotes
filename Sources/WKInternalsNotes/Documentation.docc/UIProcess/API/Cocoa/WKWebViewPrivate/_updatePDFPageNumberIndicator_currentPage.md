# ``WKInternalsNotes/WKWebView/_updatePDFPageNumberIndicator(_:currentPage:)``

`_updatePDFPageNumberIndicator` を更新する。

## Objective-C Declaration
```objective-c
- (void)_updatePDFPageNumberIndicator:(WebKit::PDFPluginIdentifier)identifier currentPage:(size_t)pageIndex;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewInternal.h#L623`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L623)
- [`API/Cocoa/WKWebView.mm#L3117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
