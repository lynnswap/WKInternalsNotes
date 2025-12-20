# ``WKInternalsNotes/_WKWebAuthenticationPanel/exportLocalAuthenticatorCredentialWithID(_:error:)``

credentialID から credential blob をエクスポートする。

## Objective-C Declaration
```objective-c
+ (NSData *)exportLocalAuthenticatorCredentialWithID:(NSData *)credentialID error:(NSError **)error WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`exportLocalAuthenticatorCredentialWithGroupAndID:credential:error:` を `group:nil` で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L144)
- [`_WKWebAuthenticationPanel.mm#L731`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L731)
- [`_WKWebAuthenticationPanel.mm#L733`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L733)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
