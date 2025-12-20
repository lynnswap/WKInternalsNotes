# ``WKInternalsNotes/_WKWebAuthenticationPanel/isUserVerifyingPlatformAuthenticatorAvailable()``

プラットフォーム認証器の利用可否を返す。

## Objective-C Declaration
```objective-c
+ (BOOL)isUserVerifyingPlatformAuthenticatorAvailable WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合は `LocalService::isAvailable()` を返し、無効時は `NO` を返す。

## References
- [`_WKWebAuthenticationPanel.h#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L149)
- [`_WKWebAuthenticationPanel.mm#L1163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1163)
- [`_WKWebAuthenticationPanel.mm#L1166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1166)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
