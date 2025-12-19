# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:didCreateBackgroundWebView:forExtensionContext:)``

バックグラウンド WebView の生成を通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller didCreateBackgroundWebView:(WKWebView *)webView forExtensionContext:(WKWebExtensionContext *)context;
```

## Discussion
背景 WebView を生成して delegate/inspectable を設定した後、delegate が実装していれば呼び出す。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L67)
- [`WebExtensionContextCocoa.mm#L2439`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/WebExtensionContextCocoa.mm#L2439)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
