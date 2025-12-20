# ``WKInternalsNotes/_WKResourceLoadDelegate/webView(_:resourceLoad:didPerformHTTPRedirection:newRequest:)``

HTTP リダイレクトを通知する。

## Objective-C Declaration
```objective-c
- (void)webView:(WKWebView *)webView resourceLoad:(_WKResourceLoadInfo *)resourceLoad didPerformHTTPRedirection:(NSURLResponse *)response newRequest:(NSURLRequest *)request;
```

## Discussion
`ResourceResponse` と `ResourceRequest` を `NSURLResponse`/`NSURLRequest` に変換し、リダイレクト先リクエストを通知する。

## References
- [`_WKResourceLoadDelegate.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadDelegate.h#L41)
- [`ResourceLoadDelegate.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L94)
- [`ResourceLoadDelegate.mm#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L103)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
