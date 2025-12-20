# ``WKInternalsNotes/_WKWebAuthenticationPanel/importLocalAuthenticatorWithAccessGroup(_:credential:error:)``

指定した access group に credential blob をインポートして credentialID を返す。

## Objective-C Declaration
```objective-c
+ (NSData *)importLocalAuthenticatorWithAccessGroup:(NSString *)accessGroup credential:(NSData *)credentialBlob error:(NSError **)error WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
CBOR を解析して必須項目（privateKey/keyType/keySize/rpID/applicationTag）を検証し、`SecKeyCreateWithData` で秘密鍵を生成する。公開鍵の SHA-1 ハッシュを `credentialID` として算出し、Keychain に同一 ID が無いことを確認して追加する。エラー時は `WKErrorMalformedCredential` / `WKErrorDuplicateCredential` / `WKErrorUnknown` を設定する。

## References
- [`_WKWebAuthenticationPanel.h#L147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L147)
- [`_WKWebAuthenticationPanel.mm#L599`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L599)
- [`_WKWebAuthenticationPanel.mm#L703`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L703)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
