# ``WKInternalsNotes/_WKAuthenticatorAttestationResponse/attestationObject``

Attestation object を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, readonly) NSData *attestationObject;
```

## Default Value
初期化時に渡された値を保持する。

## Discussion
初期化時に `attestationObject` を `retain` して保持する。

## References
- [`_WKAuthenticatorAttestationResponse.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.h#L35)
- [`_WKAuthenticatorAttestationResponse.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
