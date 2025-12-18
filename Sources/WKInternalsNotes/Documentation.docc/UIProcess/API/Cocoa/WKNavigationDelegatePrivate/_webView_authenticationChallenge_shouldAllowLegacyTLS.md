# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:authenticationChallenge:shouldAllowLegacyTLS:)``

レガシー TLS を許可するか判断する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView authenticationChallenge:(NSURLAuthenticationChallenge *)challenge shouldAllowLegacyTLS:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
NavigationState::NavigationClient::shouldAllowLegacyTLS が delegate の実装を確認し、CompletionHandlerCallChecker 付きで呼び出す。未実装の場合は data store の設定値で継続し、Deprecated TLS 版の delegate があればそちらを優先する。

## References
- [`WKNavigationDelegatePrivate.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L84)
- [`NavigationState.mm#L1215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
