# ``WKInternalsNotes/WKUIDelegatePrivate/_hostSceneBundleIdentifierForWebView(_:)``

WebView のホストシーンの bundle identifier を返す。

## Objective-C Declaration
```objective-c
- (NSString *)_hostSceneBundleIdentifierForWebView:(WKWebView *)webView WK_API_AVAILABLE(ios(17.4), visionos(1.1));
```

## Discussion
NetworkProcessProxy が Apple Pay Remote UI の presentation 情報取得時に delegate から取得し、bundle identifier を上書きする。

## References
- [`WKUIDelegatePrivate.h#L271`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L271)
- [`NetworkProcessProxyCocoa.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Network/NetworkProcessProxyCocoa.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
