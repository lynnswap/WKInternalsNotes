# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didReceiveConsoleLogForTesting:)``

テスト用のコンソールログを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didReceiveConsoleLogForTesting:(NSString *)log WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
UIClient がログ文字列を `NSString` に変換して delegate へ渡す。

## References
- [`WKUIDelegatePrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L141)
- [`UIDelegate.mm#L1994`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1994)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
