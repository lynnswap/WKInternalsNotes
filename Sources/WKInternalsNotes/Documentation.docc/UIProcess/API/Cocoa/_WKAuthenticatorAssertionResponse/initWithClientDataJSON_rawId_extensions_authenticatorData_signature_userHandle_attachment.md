# ``WKInternalsNotes/_WKAuthenticatorAssertionResponse/initWithClientDataJSON(_:rawId:extensions:authenticatorData:signature:userHandle:attachment:)``

extensions を指定して assertion response を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithClientDataJSON:(NSData *)clientDataJSON rawId:(NSData *)rawId extensions:(RetainPtr<_WKAuthenticationExtensionsClientOutputs>&&)extensions authenticatorData:(NSData *)authenticatorData signature:(NSData *)signature userHandle:(NSData * _Nullable)userHandle attachment:(_WKAuthenticatorAttachment)attachment;
```

## Discussion
`_WKAuthenticatorResponse` の初期化子に `clientDataJSON` / `rawId` / `extensions` / `attachment` を渡し、`authenticatorData` / `signature` / `userHandle` を `retain` して保持する。`userHandle` は `nil` の可能性がある。

## References
- [`_WKAuthenticatorAssertionResponseInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponseInternal.h#L37)
- [`_WKAuthenticatorAssertionResponse.mm#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.mm#L35)
- [`_WKAuthenticatorAssertionResponse.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
