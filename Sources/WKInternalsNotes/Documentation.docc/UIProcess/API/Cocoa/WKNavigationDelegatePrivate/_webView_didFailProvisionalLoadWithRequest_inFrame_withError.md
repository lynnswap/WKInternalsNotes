# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didFailProvisionalLoadWithRequest:inFrame:withError:)``

フレームの仮ロード失敗を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFailProvisionalLoadWithRequest:(NSURLRequest *)request inFrame:(WKFrameInfo *)frame withError:(NSError *)error WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
didFailProvisionalLoadWithErrorForFrame で recovery attempter 付きエラーを作成し、request と FrameInfo を渡して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L104)
- [`NavigationState.mm#L971`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L971)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
