# ``WKInternalsNotes/_WKWebAuthenticationPanelDelegate/panel(_:decidePolicyForLocalAuthenticatorWithCompletionHandler:)``

ローカル認証器の利用可否ポリシーを決定する。

## Objective-C Declaration
```objective-c
- (void)panel:(_WKWebAuthenticationPanel *)panel decidePolicyForLocalAuthenticatorWithCompletionHandler:(void (^)(_WKLocalAuthenticatorPolicy policy))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`WebAuthenticationPanelClient::decidePolicyForLocalAuthenticator` から呼ばれる。delegate が未設定または未実装の場合は `LocalAuthenticatorPolicy::Disallow` を返す。実装済みの場合は `CompletionHandlerCallChecker` を使って一度だけ完了させ、`_WKLocalAuthenticatorPolicy` を内部列挙に変換して返す。

## References
- [`_WKWebAuthenticationPanel.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L125)
- [`WebAuthenticationPanelClient.mm#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L237)
- [`WebAuthenticationPanelClient.mm#L255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L255)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
