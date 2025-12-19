# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didPromptForStorageAccess:forSubFrameDomain:forQuirk:)``

ストレージアクセスのプロンプト発生を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didPromptForStorageAccess:(NSString *)topFrameDomain forSubFrameDomain:(NSString *)subFrameDomain forQuirk:(BOOL)forQuirk WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Discussion
didPromptForStorageAccess でドメインを NSString に変換し、quirk フラグとともに呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L87)
- [`NavigationState.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
