# ``WKInternalsNotes/_WKAuthenticatorAssertionResponse/initWithClientDataJSON(_:rawId:extensionOutputsCBOR:authenticatorData:signature:userHandle:attachment:)``

extensionOutputsCBOR を指定して assertion response を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithClientDataJSON:(NSData *)clientDataJSON rawId:(NSData *)rawId extensionOutputsCBOR:(NSData *)extensionOutputsCBOR authenticatorData:(NSData *)authenticatorData signature:(NSData *)signature userHandle:(NSData * _Nullable)userHandle attachment:(_WKAuthenticatorAttachment)attachment;
```

## Discussion
`_WKAuthenticatorResponse` の初期化子に `clientDataJSON` / `rawId` / `extensionOutputsCBOR` / `attachment` を渡し、`authenticatorData` / `signature` / `userHandle` を `retain` して保持する。`userHandle` は `nil` の可能性がある。

## References
- [`_WKAuthenticatorAssertionResponseInternal.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponseInternal.h#L39)
- [`_WKAuthenticatorAssertionResponse.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.mm#L46)
- [`_WKAuthenticatorAssertionResponse.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
