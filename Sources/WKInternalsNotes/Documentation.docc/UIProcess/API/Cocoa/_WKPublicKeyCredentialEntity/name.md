# ``WKInternalsNotes/_WKPublicKeyCredentialEntity/name``

エンティティの表示名を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *name;
```

## Default Value
`initWithName:` で指定された値が設定される。

## Discussion
`initWithName:` で受け取った `name` を `self.name` に設定する。`copy` 属性のため文字列をコピー保持する。

## References
- [`_WKPublicKeyCredentialEntity.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialEntity.h#L41)
- [`_WKPublicKeyCredentialEntity.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialEntity.mm#L31)
- [`_WKPublicKeyCredentialEntity.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialEntity.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
