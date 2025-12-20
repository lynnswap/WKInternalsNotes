# ``WKInternalsNotes/_WKAuthenticatorSelectionCriteria/authenticatorAttachment``

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
- [`_WKAuthenticatorSelectionCriteria.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L41)
- [`_WKAuthenticatorSelectionCriteria.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L42)
- [`_WKAuthenticatorSelectionCriteria.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L31)
- [`_WKAuthenticatorSelectionCriteria.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
