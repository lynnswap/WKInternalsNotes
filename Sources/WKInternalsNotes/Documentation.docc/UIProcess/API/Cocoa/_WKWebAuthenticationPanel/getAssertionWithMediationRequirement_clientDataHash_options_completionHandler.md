# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAssertionWithMediationRequirement(_:clientDataHash:options:completionHandler:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)getAssertionWithMediationRequirement:(_WKWebAuthenticationMediationRequirement)mediation clientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialRequestOptions *)options completionHandler:(void (^)(_WKAuthenticatorAssertionResponse * _Nullable, NSError * _Nullable))handler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKWebAuthenticationPanel.h#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L172)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
