# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didAttachLocalInspector:)``

ローカルインスペクタのアタッチを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didAttachLocalInspector:(_WKInspector *)inspector WK_API_AVAILABLE(macos(12.0));
```

## Discussion
UIClient が `WebInspectorUIProxy` を渡して delegate に通知する。

## References
- [`WKUIDelegatePrivate.h#L326`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L326)
- [`UIDelegate.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
