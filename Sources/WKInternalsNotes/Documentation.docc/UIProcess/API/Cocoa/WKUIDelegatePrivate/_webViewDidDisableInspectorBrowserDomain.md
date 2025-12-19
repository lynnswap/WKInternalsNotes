# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidDisableInspectorBrowserDomain(_:)``

Inspector の Browser domain 無効化を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidDisableInspectorBrowserDomain:(WKWebView *)webView WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
UIDelegate::UIClient の `didDisableInspectorBrowserDomain` から delegate へ通知する。

## References
- [`WKUIDelegatePrivate.h#L205`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L205)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
