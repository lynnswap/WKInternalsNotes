# ``WKInternalsNotes/WKWebView/_didLoadNonAppInitiatedRequest(_:)``

`_didLoadNonAppInitiatedRequest` を実行する。

## Objective-C Declaration
```objective-c
- (void)_didLoadNonAppInitiatedRequest:(void (^)(BOOL result))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L510`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L510)
- [`API/Cocoa/WKWebView.mm#L4779`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4779)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
