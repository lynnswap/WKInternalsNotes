# ``WKInternalsNotes/_WKAuthenticatorResponse/initWithClientDataJSON(_:rawId:extensions:attachment:)``

クライアントデータと拡張出力、アタッチメントを保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithClientDataJSON:(NSData *)clientDataJSON rawId:(NSData *)rawId extensions:(RetainPtr<_WKAuthenticationExtensionsClientOutputs>&&)extensions attachment:(_WKAuthenticatorAttachment)attachment;
```

## Discussion
`[super init]` の成功後に `clientDataJSON` と `rawId` を retain し、`extensions` をムーブして保持し、`attachment` を保存する。

## References
- [`_WKAuthenticatorResponseInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponseInternal.h#L37)
- [`_WKAuthenticatorResponse.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
