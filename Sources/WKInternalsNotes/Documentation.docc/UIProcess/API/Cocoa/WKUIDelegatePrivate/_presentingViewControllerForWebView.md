# ``WKInternalsNotes/WKUIDelegatePrivate/_presentingViewControllerForWebView(_:)``

WebView の提示に使う view controller を返す。

## Objective-C Declaration
```objective-c
- (UIViewController *)_presentingViewControllerForWebView:(WKWebView *)webView WK_API_AVAILABLE(ios(10.0));
```

## Discussion
UIClient が `_presentingViewControllerForWebView` を呼び出して提示先を取得し、SOAuthorizationSession では埋め込み承認ビューの可否判断に利用される。

## References
- [`WKUIDelegatePrivate.h#L268`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L268)
- [`UIDelegate.mm#L1715`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1715)
- [`SOAuthorizationSession.mm#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/SOAuthorization/SOAuthorizationSession.mm#L262)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
