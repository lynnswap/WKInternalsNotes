# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataHash(_:options:userVerificationAvailability:)``

clientDataHash から MakeCredential の CBOR コマンドを生成する（拡張は未指定）。

## Objective-C Declaration
```objective-c
+ (NSData *)encodeMakeCredentialCommandWithClientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialCreationOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`encodeMakeCredentialCommandWithClientDataHash:options:userVerificationAvailability:authenticatorSupportedExtensions:` を `authenticatorSupportedExtensions:nil` で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L159)
- [`_WKWebAuthenticationPanel.mm#L1228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1228)
- [`_WKWebAuthenticationPanel.mm#L1230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1230)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
