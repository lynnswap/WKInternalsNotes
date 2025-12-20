# ``WKInternalsNotes/_WKWebAuthenticationPanel/makeCredentialWithClientDataHash(_:options:completionHandler:)``

mediation を optional として MakeCredential を実行する。

## Objective-C Declaration
```objective-c
- (void)makeCredentialWithClientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialCreationOptions *)options completionHandler:(void (^)(_WKAuthenticatorAttestationResponse * _Nullable, NSError * _Nullable))handler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`makeCredentialWithMediationRequirement:clientDataHash:options:completionHandler:` を `_WKWebAuthenticationMediationRequirementOptional` で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L168)
- [`_WKWebAuthenticationPanel.mm#L1090`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1090)
- [`_WKWebAuthenticationPanel.mm#L1092`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1092)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
