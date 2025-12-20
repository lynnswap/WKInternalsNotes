# ``WKInternalsNotes/_WKWebAuthenticationPanel/makeCredentialWithMediationRequirement(_:clientDataHash:options:completionHandler:)``

mediation と clientDataHash を指定して MakeCredential を実行する。

## Objective-C Declaration
```objective-c
- (void)makeCredentialWithMediationRequirement:(_WKWebAuthenticationMediationRequirement)mediation clientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialCreationOptions *)options completionHandler:(void (^)(_WKAuthenticatorAttestationResponse *  _Nullable, NSError *  _Nullable))handler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`clientDataHash` と `convertToCoreCreationOptionsWithOptions` の変換結果を使って `API::WebAuthenticationPanel::handleRequest` に渡す。完了時は `_WKAuthenticatorAttestationResponse` に変換して返し、例外は `WKErrorDomain` の `NSError` に変換する。`clientDataJSON` は応答に含めない。

## References
- [`_WKWebAuthenticationPanel.h#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L169)
- [`_WKWebAuthenticationPanel.mm#L1076`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1076)
- [`_WKWebAuthenticationPanel.mm#L1086`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1086)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
