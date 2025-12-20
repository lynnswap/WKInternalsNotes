# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAssertionWithChallenge(_:origin:options:completionHandler:)``

challenge と origin から clientDataJSON を生成して GetAssertion を実行する。

## Objective-C Declaration
```objective-c
- (void)getAssertionWithChallenge:(NSData *)challenge origin:(NSString *)origin options:(_WKPublicKeyCredentialRequestOptions *)options completionHandler:(void (^)(_WKAuthenticatorAssertionResponse * _Nullable, NSError * _Nullable))handler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`produceClientDataJson` で `clientDataJSON` を生成し、`produceClientDataJsonHash` の結果と `convertToCoreRequestOptionsWithOptions` の変換結果を使って `API::WebAuthenticationPanel::handleRequest` に渡す。完了時は `_WKAuthenticatorAssertionResponse` に変換して返し、例外は `WKErrorDomain` の `NSError` に変換する。

## References
- [`_WKWebAuthenticationPanel.h#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L170)
- [`_WKWebAuthenticationPanel.mm#L1128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1128)
- [`_WKWebAuthenticationPanel.mm#L1140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1140)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
