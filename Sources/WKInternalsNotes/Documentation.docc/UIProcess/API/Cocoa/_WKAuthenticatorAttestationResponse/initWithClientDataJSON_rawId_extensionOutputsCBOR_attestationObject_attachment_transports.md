# ``WKInternalsNotes/_WKAuthenticatorAttestationResponse/initWithClientDataJSON(_:rawId:extensionOutputsCBOR:attestationObject:attachment:transports:)``

extensionOutputsCBOR を指定して attestation response を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithClientDataJSON:(NSData *)clientDataJSON rawId:(NSData *)rawId extensionOutputsCBOR:(NSData *)extensions attestationObject:(NSData *)attestationObject attachment:(_WKAuthenticatorAttachment)attachment transports:(NSArray<NSNumber *> *)transports;
```

## Discussion
`_WKAuthenticatorResponse` の初期化子に `clientDataJSON` / `rawId` / `extensionOutputsCBOR` / `attachment` を渡し、`attestationObject` を `retain`、`transports` を `copy` して保持する。

## References
- [`_WKAuthenticatorAttestationResponseInternal.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponseInternal.h#L39)
- [`_WKAuthenticatorAttestationResponse.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.mm#L45)
- [`_WKAuthenticatorAttestationResponse.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
