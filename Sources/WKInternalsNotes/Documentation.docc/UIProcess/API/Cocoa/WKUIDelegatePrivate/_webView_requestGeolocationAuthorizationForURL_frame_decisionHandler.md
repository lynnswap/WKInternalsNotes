# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestGeolocationAuthorizationForURL:frame:decisionHandler:)``

指定 URL の位置情報許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestGeolocationAuthorizationForURL:(NSURL *)url frame:(WKFrameInfo *)frame decisionHandler:(void (^)(BOOL authorized))decisionHandler WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKGeolocationProviderIOS が `WKFrameInfo` を作成し、`CompletionHandlerCallChecker` で結果を受け取って `geolocationAuthorizationGranted` を通知する。

## References
- [`WKUIDelegatePrivate.h#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L238)
- [`WKGeolocationProviderIOS.mm#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L199)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
