# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didCommitLoadWithRequest:inFrame:)``

フレームのロードコミットを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didCommitLoadWithRequest:(NSURLRequest *)request inFrame:(WKFrameInfo *)frame WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
didCommitLoadForFrame で request を `DoNotUpdateHTTPBody` で NSURLRequest 化し、FrameInfo を生成して渡す。

## References
- [`WKNavigationDelegatePrivate.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L105)
- [`NavigationState.mm#L1000`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1000)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
