# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataHash(_:options:userVerificationAvailability:authenticatorSupportedExtensions:)``

clientDataHash と options から MakeCredential の CBOR コマンドを生成する。

## Objective-C Declaration
```objective-c
+ (NSData *)encodeMakeCredentialCommandWithClientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialCreationOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability authenticatorSupportedExtensions:(nullable NSArray<NSString *> *)authenticatorSupportedExtensions WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`convertToCoreCreationOptionsWithOptions` の変換結果と `userVerificationAvailability` を使って `fido::encodeMakeCredentialRequestAsCBOR` に渡す。`authenticatorSupportedExtensions` は文字列配列に変換して渡し、`ENABLE(WEB_AUTHN)` が無効な場合は `nil` を返す。

## References
- [`_WKWebAuthenticationPanel.h#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L160)
- [`_WKWebAuthenticationPanel.mm#L1233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1233)
- [`_WKWebAuthenticationPanel.mm#L1237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1237)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
