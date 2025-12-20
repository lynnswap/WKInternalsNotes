# ``WKInternalsNotes/_WKPublicKeyCredentialCreationOptions/user``

ユーザー情報を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) _WKPublicKeyCredentialUserEntity *user;
```

## Default Value
`initWithRelyingParty:user:publicKeyCredentialParamaters:` で指定された値が設定される。

## Discussion
`initWithRelyingParty:user:publicKeyCredentialParamaters:` で `user` を `self.user` に設定する。

## References
- [`_WKPublicKeyCredentialCreationOptions.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L56)
- [`_WKPublicKeyCredentialCreationOptions.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L34)
- [`_WKPublicKeyCredentialCreationOptions.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
