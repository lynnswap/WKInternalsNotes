# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didFinishLoadWithRequest:inFrame:)``

フレームのロード完了を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFinishLoadWithRequest:(NSURLRequest *)request inFrame:(WKFrameInfo *)frame WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
didFinishLoadForFrame で request を `DoNotUpdateHTTPBody` で NSURLRequest 化し、FrameInfo を生成して渡す。

## References
- [`WKNavigationDelegatePrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L107)
- [`NavigationState.mm#L1047`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1047)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
