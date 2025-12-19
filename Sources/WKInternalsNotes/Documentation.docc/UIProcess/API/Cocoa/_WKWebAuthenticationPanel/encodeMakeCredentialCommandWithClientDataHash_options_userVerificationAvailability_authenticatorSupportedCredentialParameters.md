# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataHash(_:options:userVerificationAvailability:authenticatorSupportedCredentialParameters:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
+ (NSData *) encodeMakeCredentialCommandWithClientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialCreationOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability authenticatorSupportedCredentialParameters:(NSArray<_WKPublicKeyCredentialParameters *> *)credentialParameters WK_API_AVAILABLE(macos(26.0), ios(26.0));
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
