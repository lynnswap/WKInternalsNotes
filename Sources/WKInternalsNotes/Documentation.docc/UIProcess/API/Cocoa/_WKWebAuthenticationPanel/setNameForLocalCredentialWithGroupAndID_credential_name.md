# ``WKInternalsNotes/_WKWebAuthenticationPanel/setNameForLocalCredentialWithGroupAndID(_:credential:name:)``

credential の name を更新する。

## Objective-C Declaration
```objective-c
+ (void)setNameForLocalCredentialWithGroupAndID:(NSString * _Nullable)group credential:(NSData *)credentialID name:(NSString *)name WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
Keychain から対象 credential の属性を取得し、`kSecAttrApplicationTag` に格納された CBOR のユーザーマップから `kEntityNameMapKey` を更新して `SecItemUpdate` で書き戻す。代替属性が必要な場合は `kSecAttrAlias` と `kSecAttrApplicationLabel` の両方を試す。

## References
- [`_WKWebAuthenticationPanel.h#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L142)
- [`_WKWebAuthenticationPanel.mm#L514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L514)
- [`_WKWebAuthenticationPanel.mm#L578`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L578)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
