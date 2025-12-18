# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidEnableInspectorBrowserDomain(_:)``

Inspector の Browser domain 有効化を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidEnableInspectorBrowserDomain:(WKWebView *)webView WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
UIDelegate::UIClient の `didEnableInspectorBrowserDomain` から delegate へ通知する。

## References
- [`WKUIDelegatePrivate.h#L204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L204)
- [`UIDelegate.mm#L1972`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1972)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
