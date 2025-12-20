# ``WKInternalsNotes/_WKResourceLoadDelegate/webView(_:resourceLoad:didCompleteWithError:response:)``

ロード完了を通知する。

## Objective-C Declaration
```objective-c
- (void)webView:(WKWebView *)webView resourceLoad:(_WKResourceLoadInfo *)resourceLoad didCompleteWithError:(nullable NSError *)error response:(nullable NSURLResponse *)response;
```

## Discussion
`NSError` と `NSURLResponse` を渡して完了を通知する。

## References
- [`_WKResourceLoadDelegate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadDelegate.h#L44)
- [`ResourceLoadDelegate.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L130)
- [`ResourceLoadDelegate.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/ResourceLoadDelegate.mm#L139)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
