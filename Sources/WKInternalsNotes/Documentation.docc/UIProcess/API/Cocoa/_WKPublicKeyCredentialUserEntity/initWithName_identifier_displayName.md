# ``WKInternalsNotes/_WKPublicKeyCredentialUserEntity/initWithName(_:identifier:displayName:)``

name/identifier/displayName を指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithName:(NSString *)name identifier:(NSData *)identifier displayName:(NSString *)displayName;
```

## Discussion
`super initWithName:` を呼び、`identifier` と `displayName` をそれぞれ設定する。

## References
- [`_WKPublicKeyCredentialUserEntity.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.h#L38)
- [`_WKPublicKeyCredentialUserEntity.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.mm#L31)
- [`_WKPublicKeyCredentialUserEntity.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.mm#L36)
- [`_WKPublicKeyCredentialUserEntity.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.mm#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
