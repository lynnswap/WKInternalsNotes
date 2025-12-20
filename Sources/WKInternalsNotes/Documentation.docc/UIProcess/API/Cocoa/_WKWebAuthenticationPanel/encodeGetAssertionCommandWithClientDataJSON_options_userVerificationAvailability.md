# ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeGetAssertionCommandWithClientDataJSON(_:options:userVerificationAvailability:)``

clientDataJSON から GetAssertion の CBOR コマンドを生成する（拡張は未指定）。

## Objective-C Declaration
```objective-c
+ (NSData *)encodeGetAssertionCommandWithClientDataJSON:(NSData *)clientDataJSON options:(_WKPublicKeyCredentialRequestOptions *)options userVerificationAvailability:(_WKWebAuthenticationUserVerificationAvailability)userVerificationAvailability WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`encodeGetAssertionCommandWithClientDataJSON:options:userVerificationAvailability:authenticatorSupportedExtensions:` を `authenticatorSupportedExtensions:nil` で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L156)
- [`_WKWebAuthenticationPanel.mm#L1211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1211)
- [`_WKWebAuthenticationPanel.mm#L1213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
