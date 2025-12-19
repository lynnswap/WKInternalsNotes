# ``WKInternalsNotes/WKWebView/_reloadExpiredOnly()``

`_reloadExpiredOnly` を実行する。

## Objective-C Declaration
```objective-c
- (WKNavigation *)_reloadExpiredOnly WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L352`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L352)
- [`API/Cocoa/WKWebView.mm#L4925`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4925)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
