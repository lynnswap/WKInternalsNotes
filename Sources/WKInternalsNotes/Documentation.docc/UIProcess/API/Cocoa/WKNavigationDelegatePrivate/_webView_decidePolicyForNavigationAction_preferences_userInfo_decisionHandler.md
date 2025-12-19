# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:decidePolicyForNavigationAction:preferences:userInfo:decisionHandler:)``

ナビゲーションアクションのポリシーを決定する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction preferences:(WKWebpagePreferences *)preferences userInfo:(id <NSSecureCoding>)userInfo decisionHandler:(void (^)(WKNavigationActionPolicy, WKWebpagePreferences *))decisionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
NavigationState::NavigationClient が delegate 実装を確認し、preferences と decisionHandler を渡して呼び出す。private 版は userInfo を引数に取るが、現行実装では nil を渡している。

## References
- [`WKNavigationDelegatePrivate.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L72)
- [`NavigationState.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
