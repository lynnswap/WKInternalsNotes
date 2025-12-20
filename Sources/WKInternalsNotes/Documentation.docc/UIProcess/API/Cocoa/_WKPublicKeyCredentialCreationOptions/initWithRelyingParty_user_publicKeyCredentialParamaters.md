# ``WKInternalsNotes/_WKPublicKeyCredentialCreationOptions/initWithRelyingParty(_:user:publicKeyCredentialParamaters:)``

relyingParty/user/parameters を指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithRelyingParty:(_WKPublicKeyCredentialRelyingPartyEntity *)relyingParty user:(_WKPublicKeyCredentialUserEntity *)user publicKeyCredentialParamaters:(NSArray<_WKPublicKeyCredentialParameters *> *)publicKeyCredentialParamaters;
```

## Discussion
`relyingParty` / `user` / `publicKeyCredentialParamaters` をそれぞれ保持する。

## References
- [`_WKPublicKeyCredentialCreationOptions.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L53)
- [`_WKPublicKeyCredentialCreationOptions.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L34)
- [`_WKPublicKeyCredentialCreationOptions.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L39)
- [`_WKPublicKeyCredentialCreationOptions.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
