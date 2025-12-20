# ``WKInternalsNotes/_WKAuthenticatorAttestationResponse/transports``

Authenticator の transports を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<NSNumber *> *transports;
```

## Default Value
未設定の場合は `nil`。

## Discussion
初期化時に `transports` を `copy` して保持する。

## References
- [`_WKAuthenticatorAttestationResponse.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.h#L36)
- [`_WKAuthenticatorAttestationResponse.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAttestationResponse.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
