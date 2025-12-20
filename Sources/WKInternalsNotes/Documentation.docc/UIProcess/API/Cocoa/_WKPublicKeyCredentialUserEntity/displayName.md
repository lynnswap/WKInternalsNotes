# ``WKInternalsNotes/_WKPublicKeyCredentialUserEntity/displayName``

ユーザーの表示名を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *displayName;
```

## Default Value
`initWithName:identifier:displayName:` で指定された値が設定される。

## Discussion
`initWithName:identifier:displayName:` で `displayName` を `self.displayName` に設定する。`copy` 属性のため文字列をコピー保持する。

## References
- [`_WKPublicKeyCredentialUserEntity.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.h#L41)
- [`_WKPublicKeyCredentialUserEntity.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.mm#L31)
- [`_WKPublicKeyCredentialUserEntity.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.mm#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
