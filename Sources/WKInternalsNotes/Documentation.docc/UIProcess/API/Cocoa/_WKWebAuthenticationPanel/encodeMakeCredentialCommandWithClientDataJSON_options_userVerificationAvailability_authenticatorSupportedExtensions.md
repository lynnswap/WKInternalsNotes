# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataJSON(_:options:userVerificationAvailability:authenticatorSupportedExtensions:)``

clientDataJSON と options から MakeCredential の CBOR コマンドを生成する。

## Objective-C Declaration
```objective-c
+ (NSData *)encodeMakeCredentialCommandWithClientDataJSON:(NSData *)clientDataJSON options:(_WKPublicKeyCredentialCreationOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability authenticatorSupportedExtensions:(nullable NSArray<NSString *> *)authenticatorSupportedExtensions WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`clientDataJSON` をハッシュ化し、`convertToCoreCreationOptionsWithOptions` の変換結果と `userVerificationAvailability` を使って `fido::encodeMakeCredentialRequestAsCBOR` に渡す。`authenticatorSupportedExtensions` は文字列配列に変換して渡し、`ENABLE(WEB_AUTHN)` が無効な場合は `nil` を返す。

## References
- [`_WKWebAuthenticationPanel.h#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L155)
- [`_WKWebAuthenticationPanel.mm#L1199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1199)
- [`_WKWebAuthenticationPanel.mm#L1204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1204)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
