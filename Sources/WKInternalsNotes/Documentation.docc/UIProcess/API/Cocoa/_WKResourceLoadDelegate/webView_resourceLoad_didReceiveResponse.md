# ``WKInternalsNotes/_WKResourceLoadDelegate/webView(_:resourceLoad:didReceiveResponse:)``

レスポンス受信を通知する。

## Objective-C Declaration
```objective-c
- (void)webView:(WKWebView *)webView resourceLoad:(_WKResourceLoadInfo *)resourceLoad didReceiveResponse:(NSURLResponse *)response;
```

## Discussion
`ResourceResponse` を `NSURLResponse` に変換して通知する。

## References
- [`_WKResourceLoadDelegate.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadDelegate.h#L43)
- [`ResourceLoadDelegate.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L118)
- [`ResourceLoadDelegate.mm#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L127)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
