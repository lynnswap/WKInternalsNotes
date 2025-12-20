# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAssertionWithMediationRequirement(_:clientDataHash:options:completionHandler:)``

mediation と clientDataHash を指定して GetAssertion を実行する。

## Objective-C Declaration
```objective-c
- (void)getAssertionWithMediationRequirement:(_WKWebAuthenticationMediationRequirement)mediation clientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialRequestOptions *)options completionHandler:(void (^)(_WKAuthenticatorAssertionResponse * _Nullable, NSError * _Nullable))handler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`clientDataHash` と `convertToCoreRequestOptionsWithOptions` の変換結果を使って `API::WebAuthenticationPanel::handleRequest` に渡す。完了時は `_WKAuthenticatorAssertionResponse` に変換して返し、例外は `WKErrorDomain` の `NSError` に変換する。`clientDataJSON` は応答に含めない。

## References
- [`_WKWebAuthenticationPanel.h#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L172)
- [`_WKWebAuthenticationPanel.mm#L1144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1144)
- [`_WKWebAuthenticationPanel.mm#L1154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
