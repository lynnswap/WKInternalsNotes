# ``WKInternalsNotes/_WKWebAuthenticationPanel/deleteLocalAuthenticatorCredentialWithID(_:)``

credentialID を指定してローカル認証器の credential を削除する。

## Objective-C Declaration
```objective-c
+ (void)deleteLocalAuthenticatorCredentialWithID:(NSData *)credentialID WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`deleteLocalAuthenticatorCredentialWithGroupAndID:credential:` を `group:nil` で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L138)
- [`_WKWebAuthenticationPanel.mm#L404`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L404)
- [`_WKWebAuthenticationPanel.mm#L406`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L406)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
