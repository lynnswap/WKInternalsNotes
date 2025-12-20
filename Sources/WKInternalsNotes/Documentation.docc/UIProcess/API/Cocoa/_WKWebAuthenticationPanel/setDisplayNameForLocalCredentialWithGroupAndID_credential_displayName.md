# ``WKInternalsNotes/_WKWebAuthenticationPanel/setDisplayNameForLocalCredentialWithGroupAndID(_:credential:displayName:)``

credential の displayName を更新する。

## Objective-C Declaration
```objective-c
+ (void)setDisplayNameForLocalCredentialWithGroupAndID:(NSString * _Nullable)group credential:(NSData *)credentialID displayName: (NSString *)displayName WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
Keychain から対象 credential の属性を取得し、`kSecAttrApplicationTag` に格納された CBOR のユーザーマップから `kDisplayNameMapKey` を更新して `SecItemUpdate` で書き戻す。代替属性が必要な場合は `kSecAttrAlias` と `kSecAttrApplicationLabel` の両方を試す。

## References
- [`_WKWebAuthenticationPanel.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L141)
- [`_WKWebAuthenticationPanel.mm#L441`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L441)
- [`_WKWebAuthenticationPanel.mm#L506`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L506)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
