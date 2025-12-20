# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataHash(_:options:userVerificationAvailability:authenticatorSupportedCredentialParameters:)``

clientDataHash と options から MakeCredential の CBOR コマンドを生成し、対応パラメータを指定する。

## Objective-C Declaration
```objective-c
+ (NSData *) encodeMakeCredentialCommandWithClientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialCreationOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability authenticatorSupportedCredentialParameters:(NSArray<_WKPublicKeyCredentialParameters *> *)credentialParameters WK_API_AVAILABLE(macos(26.0), ios(26.0));
```

## Discussion
`convertToCoreCreationOptionsWithOptions` の変換結果と `userVerificationAvailability` を使って `fido::encodeMakeCredentialRequestAsCBOR` に渡し、`credentialParameters` を `publicKeyCredentialParameters` で変換して指定する。`ENABLE(WEB_AUTHN)` が無効な場合は `nil` を返す。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L47)
- [`_WKWebAuthenticationPanel.mm#L1244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1244)
- [`_WKWebAuthenticationPanel.mm#L1249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1249)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
