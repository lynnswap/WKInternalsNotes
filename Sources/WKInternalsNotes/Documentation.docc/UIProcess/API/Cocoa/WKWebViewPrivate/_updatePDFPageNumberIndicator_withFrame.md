# ``WKInternalsNotes/WKWebView/_updatePDFPageNumberIndicator(_:withFrame:)``

`_updatePDFPageNumberIndicator` を更新する。

## Objective-C Declaration
```objective-c
- (void)_updatePDFPageNumberIndicator:(WebKit::PDFPluginIdentifier)identifier withFrame:(CGRect)rect;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L622`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L622)
- [`WKWebView.mm#L3117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
