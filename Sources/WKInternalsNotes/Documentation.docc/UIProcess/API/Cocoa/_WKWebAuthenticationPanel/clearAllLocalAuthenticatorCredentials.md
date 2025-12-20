# ``WKInternalsNotes/_WKWebAuthenticationPanel/clearAllLocalAuthenticatorCredentials()``

ローカル認証器の credential を全削除する。

## Objective-C Declaration
```objective-c
+ (void)clearAllLocalAuthenticatorCredentials WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合は `WebKit::LocalAuthenticator::clearAllCredentials()` を呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L140)
- [`_WKWebAuthenticationPanel.mm#L434`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L434)
- [`_WKWebAuthenticationPanel.mm#L437`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L437)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
