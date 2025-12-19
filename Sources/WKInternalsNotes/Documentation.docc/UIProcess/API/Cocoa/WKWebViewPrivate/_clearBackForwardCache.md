# ``WKInternalsNotes/WKWebView/_clearBackForwardCache()``

`_clearBackForwardCache` をリセットする。

## Objective-C Declaration
```objective-c
- (void)_clearBackForwardCache WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L306)
- [`API/Cocoa/WKWebView.mm#L5079`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5079)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
