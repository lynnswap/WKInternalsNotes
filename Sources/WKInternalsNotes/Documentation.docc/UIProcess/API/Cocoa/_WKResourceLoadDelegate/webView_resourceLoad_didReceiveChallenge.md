# ``WKInternalsNotes/_WKResourceLoadDelegate/webView(_:resourceLoad:didReceiveChallenge:)``

認証チャレンジを通知する。

## Objective-C Declaration
```objective-c
- (void)webView:(WKWebView *)webView resourceLoad:(_WKResourceLoadInfo *)resourceLoad didReceiveChallenge:(NSURLAuthenticationChallenge *)challenge;
```

## Discussion
`AuthenticationChallenge` を `NSURLAuthenticationChallenge` に変換し、delegate にそのまま渡す。

## References
- [`_WKResourceLoadDelegate.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadDelegate.h#L42)
- [`ResourceLoadDelegate.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L106)
- [`ResourceLoadDelegate.mm#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L115)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
