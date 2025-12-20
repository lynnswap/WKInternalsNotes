# ``WKInternalsNotes/_WKPublicKeyCredentialCreationOptions/init()``

直接初期化できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
ヘッダで `NS_UNAVAILABLE` 指定のため `init` は使用できない。`initWithRelyingParty:user:publicKeyCredentialParamaters:` を利用する。

## References
- [`_WKPublicKeyCredentialCreationOptions.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L52)
- [`_WKPublicKeyCredentialCreationOptions.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
