# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAssertionWithClientDataHash(_:options:completionHandler:)``

mediation を optional として GetAssertion を実行する。

## Objective-C Declaration
```objective-c
- (void)getAssertionWithClientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialRequestOptions *)options completionHandler:(void (^)(_WKAuthenticatorAssertionResponse * _Nullable, NSError * _Nullable))handler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`getAssertionWithMediationRequirement:clientDataHash:options:completionHandler:` を `_WKWebAuthenticationMediationRequirementOptional` で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L171)
- [`_WKWebAuthenticationPanel.mm#L1158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1158)
- [`_WKWebAuthenticationPanel.mm#L1160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
