# ``WKInternalsNotes/_WKPublicKeyCredentialCreationOptions/relyingParty``

Relying Party 情報を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) _WKPublicKeyCredentialRelyingPartyEntity *relyingParty;
```

## Default Value
`initWithRelyingParty:user:publicKeyCredentialParamaters:` で指定された値が設定される。

## Discussion
`initWithRelyingParty:user:publicKeyCredentialParamaters:` で `relyingParty` を `self.relyingParty` に設定する。

## References
- [`_WKPublicKeyCredentialCreationOptions.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L55)
- [`_WKPublicKeyCredentialCreationOptions.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L34)
- [`_WKPublicKeyCredentialCreationOptions.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
