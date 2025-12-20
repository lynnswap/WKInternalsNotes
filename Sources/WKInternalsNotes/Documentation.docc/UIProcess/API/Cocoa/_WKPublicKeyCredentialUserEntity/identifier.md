# ``WKInternalsNotes/_WKPublicKeyCredentialUserEntity/identifier``

ユーザー識別子を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSData *identifier;
```

## Default Value
`initWithName:identifier:displayName:` で指定された値が設定される。

## Discussion
`initWithName:identifier:displayName:` で `identifier` を `self.identifier` に設定する。`copy` 属性のためデータをコピー保持する。

## References
- [`_WKPublicKeyCredentialUserEntity.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.h#L40)
- [`_WKPublicKeyCredentialUserEntity.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.mm#L31)
- [`_WKPublicKeyCredentialUserEntity.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
