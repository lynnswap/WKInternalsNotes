# ``WKInternalsNotes/_WKWebAuthenticationPanel/importLocalAuthenticatorCredential(_:error:)``

credential blob をインポートして credentialID を返す。

## Objective-C Declaration
```objective-c
+ (NSData *)importLocalAuthenticatorCredential:(NSData *)credentialBlob error:(NSError **)error WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`importLocalAuthenticatorWithAccessGroup:credential:error:` を既定の access group（`LocalAuthenticatorAccessGroup`）で呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L146)
- [`_WKWebAuthenticationPanel.mm#L594`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L594)
- [`_WKWebAuthenticationPanel.mm#L596`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L596)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
