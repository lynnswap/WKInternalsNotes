# ``WKInternalsNotes/_WKPublicKeyCredentialUserEntity/new()``

直接生成できない。

## Objective-C Declaration
```objective-c
+ (instancetype)new NS_UNAVAILABLE;
```

## Discussion
ヘッダで `NS_UNAVAILABLE` 指定のため `new` は使用できない。`initWithName:identifier:displayName:` を利用する。

## References
- [`_WKPublicKeyCredentialUserEntity.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.h#L35)
- [`_WKPublicKeyCredentialUserEntity.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.h#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
