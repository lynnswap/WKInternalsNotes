# ``WKInternalsNotes/_WKPublicKeyCredentialRequestOptions/authenticatorAttachment``

認証器の接続方式の要求を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic) _WKAuthenticatorAttachment authenticatorAttachment;
```

## Default Value
既定値は `_WKAuthenticatorAttachmentAll`。

## Discussion
`init` で `_WKAuthenticatorAttachmentAll` に初期化される。

## References
- [`_WKPublicKeyCredentialRequestOptions.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.h#L47)
- [`_WKPublicKeyCredentialRequestOptions.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.h#L48)
- [`_WKPublicKeyCredentialRequestOptions.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.mm#L31)
- [`_WKPublicKeyCredentialRequestOptions.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.mm#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
