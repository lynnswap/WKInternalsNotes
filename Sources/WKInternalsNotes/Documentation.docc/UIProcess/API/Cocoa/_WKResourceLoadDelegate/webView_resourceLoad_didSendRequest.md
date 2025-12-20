# ``WKInternalsNotes/_WKResourceLoadDelegate/webView(_:resourceLoad:didSendRequest:)``

リソース要求の送信を通知する。

## Objective-C Declaration
```objective-c
- (void)webView:(WKWebView *)webView resourceLoad:(_WKResourceLoadInfo *)resourceLoad didSendRequest:(NSURLRequest *)request;
```

## Discussion
`ResourceLoadClient::didSendRequest` で `ResourceLoadInfo` をラップし、`NSURLRequest` を渡して通知する。

## References
- [`_WKResourceLoadDelegate.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadDelegate.h#L40)
- [`ResourceLoadDelegate.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L82)
- [`ResourceLoadDelegate.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L91)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
