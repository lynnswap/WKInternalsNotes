# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeGetAssertionCommandWithClientDataJSON(_:options:userVerificationAvailability:authenticatorSupportedExtensions:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
+ (NSData *)encodeGetAssertionCommandWithClientDataJSON:(NSData *)clientDataJSON options:(_WKPublicKeyCredentialRequestOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability authenticatorSupportedExtensions:(nullable NSArray<NSString *> *)authenticatorSupportedExtensions WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKWebAuthenticationPanel.h#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
