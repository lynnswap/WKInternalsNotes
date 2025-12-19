# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:navigation:didFailProvisionalLoadInSubframe:withError:)``

サブフレームの仮ロード失敗を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView navigation:(WKNavigation *)navigation didFailProvisionalLoadInSubframe:(WKFrameInfo *)subframe withError:(NSError *)error;
```

## Discussion
didFailProvisionalNavigationWithError でサブフレームの場合に `navigation:nil` を渡し、FrameInfo とエラーを通知する。

## References
- [`WKNavigationDelegatePrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L66)
- [`NavigationState.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
