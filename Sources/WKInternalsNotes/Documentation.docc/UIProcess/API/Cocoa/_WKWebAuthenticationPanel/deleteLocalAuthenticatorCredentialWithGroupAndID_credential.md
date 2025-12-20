# ``WKInternalsNotes/_WKWebAuthenticationPanel/deleteLocalAuthenticatorCredentialWithGroupAndID(_:credential:)``

access group を指定してローカル認証器の credential を削除する。

## Objective-C Declaration
```objective-c
+ (void)deleteLocalAuthenticatorCredentialWithGroupAndID:(NSString * _Nullable)group credential:(NSData *)credentialID WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、Keychain の削除クエリを構築し、`credentialID` を `kSecAttrAlias` または `kSecAttrApplicationLabel` に設定して `SecItemDelete` を実行する。代替属性が必要な場合は両方を試す。

## References
- [`_WKWebAuthenticationPanel.h#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L139)
- [`_WKWebAuthenticationPanel.mm#L409`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L409)
- [`_WKWebAuthenticationPanel.mm#L424`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L424)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
