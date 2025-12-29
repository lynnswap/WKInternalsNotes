# ``WKInternalsNotes/_WKAuthenticatorResponse/extensionOutputsCBOR``

拡張出力のCBORデータを保持する。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, copy) NSData *extensionOutputsCBOR;
```

## Default Value
`initWithClientDataJSON:rawId:extensionOutputsCBOR:attachment:` で渡したデータのコピー。未指定なら `nil`。

## Discussion
`initWithClientDataJSON:rawId:extensionOutputsCBOR:attachment:` で `extensionOutputsCBOR` を `copy` して保持する。

## References
- [`_WKAuthenticatorResponse.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.h#L44)
- [`_WKAuthenticatorResponse.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.mm#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
