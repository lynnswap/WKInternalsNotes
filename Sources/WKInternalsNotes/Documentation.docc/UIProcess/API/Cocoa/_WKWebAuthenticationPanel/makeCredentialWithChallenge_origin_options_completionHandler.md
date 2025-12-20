# ``WKInternalsNotes/_WKWebAuthenticationPanel/makeCredentialWithChallenge(_:origin:options:completionHandler:)``

challenge と origin から clientDataJSON を生成して MakeCredential を実行する。

## Objective-C Declaration
```objective-c
- (void)makeCredentialWithChallenge:(NSData *)challenge origin:(NSString *)origin options:(_WKPublicKeyCredentialCreationOptions *)options completionHandler:(void (^)(_WKAuthenticatorAttestationResponse * _Nullable, NSError * _Nullable))handler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`produceClientDataJson` で `clientDataJSON` を生成し、`produceClientDataJsonHash` の結果と `convertToCoreCreationOptionsWithOptions` の変換結果を使って `API::WebAuthenticationPanel::handleRequest` に渡す。完了時は `_WKAuthenticatorAttestationResponse` に変換して返し、例外は `WKErrorDomain` の `NSError` に変換する。

## References
- [`_WKWebAuthenticationPanel.h#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L167)
- [`_WKWebAuthenticationPanel.mm#L1060`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1060)
- [`_WKWebAuthenticationPanel.mm#L1072`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1072)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
