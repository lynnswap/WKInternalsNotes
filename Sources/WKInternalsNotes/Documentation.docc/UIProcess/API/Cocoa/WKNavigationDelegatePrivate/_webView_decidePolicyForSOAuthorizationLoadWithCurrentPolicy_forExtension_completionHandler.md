# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:decidePolicyForSOAuthorizationLoadWithCurrentPolicy:forExtension:completionHandler:)``

SO 認可ロードのポリシーを決定する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView decidePolicyForSOAuthorizationLoadWithCurrentPolicy:(_WKSOAuthorizationLoadPolicy)policy forExtension:(NSString *)extension completionHandler:(void (^)(_WKSOAuthorizationLoadPolicy policy))completionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
decidePolicyForSOAuthorizationLoad が delegate を確認し、CompletionHandlerCallChecker 付きで呼び出して policy を変換する。未実装や delegate 不在時は現在の policy をそのまま返す。

## References
- [`WKNavigationDelegatePrivate.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L103)
- [`NavigationState.mm#L226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L226)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
