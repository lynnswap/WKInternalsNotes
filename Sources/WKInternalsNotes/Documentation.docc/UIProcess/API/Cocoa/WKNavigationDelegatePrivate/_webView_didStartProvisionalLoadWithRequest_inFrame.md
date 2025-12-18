# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didStartProvisionalLoadWithRequest:inFrame:)``

フレームの仮ロード開始を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didStartProvisionalLoadWithRequest:(NSURLRequest *)request inFrame:(WKFrameInfo *)frame WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
didStartProvisionalLoadForFrame で request を `DoNotUpdateHTTPBody` で NSURLRequest 化し、FrameInfo を生成して渡す。

## References
- [`WKNavigationDelegatePrivate.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L103)
- [`NavigationState.mm#L849`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L849)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
