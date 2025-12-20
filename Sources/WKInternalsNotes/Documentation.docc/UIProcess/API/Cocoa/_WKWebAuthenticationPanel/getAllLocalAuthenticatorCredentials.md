# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentials()``

ローカル認証器の credential 一覧を返す。

## Objective-C Declaration
```objective-c
+ (NSArray<NSDictionary *> *)getAllLocalAuthenticatorCredentials WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、既定の access group（`LocalAuthenticatorAccessGroup`）で `getAllLocalAuthenticatorCredentialsImpl` を呼び出す。Keychain から取得した属性を CBOR 解析し、辞書配列として返す。無効時は `nil` を返す。

## References
- [`_WKWebAuthenticationPanel.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L134)
- [`_WKWebAuthenticationPanel.mm#L349`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L349)
- [`_WKWebAuthenticationPanel.mm#L352`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L352)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
