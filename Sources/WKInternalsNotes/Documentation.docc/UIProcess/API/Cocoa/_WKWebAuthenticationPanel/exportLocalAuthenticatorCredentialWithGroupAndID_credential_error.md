# ``WKInternalsNotes/_WKWebAuthenticationPanel/exportLocalAuthenticatorCredentialWithGroupAndID(_:credential:error:)``

指定した access group の credential を CBOR 形式でエクスポートする。

## Objective-C Declaration
```objective-c
+ (NSData *)exportLocalAuthenticatorCredentialWithGroupAndID:(NSString * _Nullable)group credential:(NSData *)credentialID error:(NSError **)error WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
Keychain から秘密鍵と属性を取得し、`privateKey`/`keyType`/`keySize`/`relyingParty`/`applicationTag` を含む CBOR マップを組み立てて返す。取得に失敗した場合は `WKErrorCredentialNotFound` または `WKErrorMalformedCredential` を設定する。

## References
- [`_WKWebAuthenticationPanel.h#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L145)
- [`_WKWebAuthenticationPanel.mm#L736`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L736)
- [`_WKWebAuthenticationPanel.mm#L805`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L805)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
