# ``WKInternalsNotes/_WKAuthenticatorAttestationResponse/initWithClientDataJSON(_:rawId:extensions:attestationObject:attachment:transports:)``

extensions を指定して attestation response を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithClientDataJSON:(NSData *)clientDataJSON rawId:(NSData *)rawId extensions:(RetainPtr<_WKAuthenticationExtensionsClientOutputs>&&)extensions attestationObject:(NSData *)attestationObject attachment:(_WKAuthenticatorAttachment)attachment transports:(NSArray<NSNumber *> *)transports;
```

## Discussion
`_WKAuthenticatorResponse` の初期化子に `clientDataJSON` / `rawId` / `extensions` / `attachment` を渡し、`attestationObject` を `retain`、`transports` を `copy` して保持する。

## References
- [`_WKAuthenticatorAttestationResponseInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponseInternal.h#L37)
- [`_WKAuthenticatorAttestationResponse.mm#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.mm#L35)
- [`_WKAuthenticatorAttestationResponse.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
