# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:contentRuleListWithIdentifier:performedAction:forURL:)``

content rule list のアクション実行を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView contentRuleListWithIdentifier:(NSString *)identifier performedAction:(_WKContentRuleListAction *)action forURL:(NSURL *)url WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
contentRuleListNotification の結果を列挙し、identifier と action を Objective-C ラッパーに変換して URL とともに呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L100)
- [`NavigationState.mm#L757`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L757)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
