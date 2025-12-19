# ``WKInternalsNotes/WKWebView/_loadRequest(_:shouldOpenExternalURLsPolicy:)``

`_loadRequest` を実行する。

## Objective-C Declaration
```objective-c
- (WKNavigation *)_loadRequest:(NSURLRequest *)request shouldOpenExternalURLsPolicy:(_WKShouldOpenExternalURLsPolicy)shouldOpenExternalURLsPolicy WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L196`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L196)
- [`WKWebView.mm#L4614`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4614)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
