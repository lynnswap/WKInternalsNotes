# ``WKInternalsNotes/WKUIDelegatePrivate/_hostSceneIdentifierForWebView(_:)``

WebView のホストシーン識別子を返す。

## Objective-C Declaration
```objective-c
- (NSString *)_hostSceneIdentifierForWebView:(WKWebView *)webView WK_API_AVAILABLE(ios(17.4), visionos(1.1));
```

## Discussion
NetworkProcessProxy で支払い UI の scene ID を取得するほか、SOAuthorizationSession で callerSceneIdentifier を authorizationOptions に追加する際に使用する。

## References
- [`WKUIDelegatePrivate.h#L269`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L269)
- [`NetworkProcessProxyCocoa.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Network/NetworkProcessProxyCocoa.mm#L149)
- [`SOAuthorizationSession.mm#L250`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/SOAuthorization/SOAuthorizationSession.mm#L250)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
