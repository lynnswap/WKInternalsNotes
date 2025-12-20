# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeGetAssertionCommandWithClientDataHash(_:options:userVerificationAvailability:)``

clientDataHash から GetAssertion の CBOR コマンドを生成する（拡張は未指定）。

## Objective-C Declaration
```objective-c
+ (NSData *)encodeGetAssertionCommandWithClientDataHash:(NSData *)clientDataHash options:(_WKPublicKeyCredentialRequestOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`encodeGetAssertionCommandWithClientDataHash:options:userVerificationAvailability:authenticatorSupportedExtensions:` を `authenticatorSupportedExtensions:nil` で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L161)
- [`_WKWebAuthenticationPanel.mm#L1257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1257)
- [`_WKWebAuthenticationPanel.mm#L1259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1259)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
