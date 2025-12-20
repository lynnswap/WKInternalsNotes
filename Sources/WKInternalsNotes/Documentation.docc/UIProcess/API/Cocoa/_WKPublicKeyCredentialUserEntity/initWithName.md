# ``WKInternalsNotes/_WKPublicKeyCredentialUserEntity/initWithName(_:)``

この初期化子は使用できない。

## Objective-C Declaration
```objective-c
- (instancetype)initWithName:(NSString *)name NS_UNAVAILABLE;
```

## Discussion
ヘッダで `NS_UNAVAILABLE` 指定のため `initWithName:` は使用できない。`identifier` と `displayName` を含む初期化子を使う。

## References
- [`_WKPublicKeyCredentialUserEntity.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.h#L37)
- [`_WKPublicKeyCredentialUserEntity.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialUserEntity.h#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
