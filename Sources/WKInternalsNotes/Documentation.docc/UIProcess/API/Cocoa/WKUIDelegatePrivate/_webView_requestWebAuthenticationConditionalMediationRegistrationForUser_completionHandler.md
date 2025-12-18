# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestWebAuthenticationConditionalMediationRegistrationForUser:completionHandler:)``

WebAuthn の条件付きメディエーション登録可否を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestWebAuthenticationConditionalMediationRegistrationForUser:(NSString *)user completionHandler:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を使って user を渡し、結果を completionHandler に返す。

## References
- [`WKUIDelegatePrivate.h#L194`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L194)
- [`UIDelegate.mm#L1880`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1880)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
