# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestCookieConsentWithMoreInfoHandler:decisionHandler:)``

Cookie 同意の判断を delegate に求める。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestCookieConsentWithMoreInfoHandler:(void (^)(void))moreInfoHandler decisionHandler:(void (^)(BOOL))decisionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
UIClient が `moreInfoHandler` を `nil` で渡し（FIXME で未対応）、`decisionHandler` の結果を Consent/Dissent に変換する。

## References
- [`WKUIDelegatePrivate.h#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L215)
- [`UIDelegate.mm#L875`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L875)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
