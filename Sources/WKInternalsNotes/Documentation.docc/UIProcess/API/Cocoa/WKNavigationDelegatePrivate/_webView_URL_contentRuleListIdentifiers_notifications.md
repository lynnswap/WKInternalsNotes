# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:URL:contentRuleListIdentifiers:notifications:)``

content rule list の通知をまとめて受け取る。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView URL:(NSURL *)url contentRuleListIdentifiers:(NSArray<NSString *> *)identifiers notifications:(NSArray<NSString *> *)notifications WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
contentRuleListNotification で results から identifiers と notifications を収集し、URL を NSURL に変換して呼び出す。通知が無い場合は呼ばれない。

## References
- [`WKNavigationDelegatePrivate.h#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L99)
- [`NavigationState.mm#L753`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L753)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
