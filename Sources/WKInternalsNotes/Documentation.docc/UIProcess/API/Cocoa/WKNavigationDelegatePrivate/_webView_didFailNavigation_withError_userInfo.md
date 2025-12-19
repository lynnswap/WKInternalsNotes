# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didFailNavigation:withError:userInfo:)``

ナビゲーション失敗を userInfo 付きで通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFailNavigation:(WKNavigation *)navigation withError:(NSError *)error userInfo:(id <NSSecureCoding>)userInfo WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
didFailNavigationWithError で recovery attempter 付きエラーを生成し、userInfo を NSSecureCoding として渡して呼び出す。private 版未実装の場合は public 版へフォールバックする。

## References
- [`WKNavigationDelegatePrivate.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L73)
- [`NavigationState.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
