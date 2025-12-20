# ``WKInternalsNotes/_WKPublicKeyCredentialRelyingPartyEntity/init()``

直接初期化できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
ヘッダで `NS_UNAVAILABLE` 指定のため `init` は使用できない。`initWithName:` を利用する。

## References
- [`_WKPublicKeyCredentialRelyingPartyEntity.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRelyingPartyEntity.h#L36)
- [`_WKPublicKeyCredentialRelyingPartyEntity.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRelyingPartyEntity.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
