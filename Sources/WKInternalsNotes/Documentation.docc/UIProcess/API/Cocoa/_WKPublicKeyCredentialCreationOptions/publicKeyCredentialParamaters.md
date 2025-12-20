# ``WKInternalsNotes/_WKPublicKeyCredentialCreationOptions/publicKeyCredentialParamaters``

公開鍵パラメータの配列を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<_WKPublicKeyCredentialParameters *> *publicKeyCredentialParamaters;
```

## Default Value
`initWithRelyingParty:user:publicKeyCredentialParamaters:` で指定された値が設定される。

## Discussion
`initWithRelyingParty:user:publicKeyCredentialParamaters:` で `publicKeyCredentialParamaters` を `self.publicKeyCredentialParamaters` に設定する。`copy` 属性のため配列をコピー保持する。

## References
- [`_WKPublicKeyCredentialCreationOptions.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L58)
- [`_WKPublicKeyCredentialCreationOptions.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L34)
- [`_WKPublicKeyCredentialCreationOptions.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
