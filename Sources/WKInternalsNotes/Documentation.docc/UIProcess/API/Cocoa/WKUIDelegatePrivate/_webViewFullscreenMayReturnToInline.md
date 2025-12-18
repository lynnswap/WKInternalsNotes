# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewFullscreenMayReturnToInline(_:)``

フルスクリーンからインライン復帰可能を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewFullscreenMayReturnToInline:(WKWebView *)webView;
```

## Discussion
UIDelegate::UIClient が fullscreen から戻れるタイミングで delegate に通知する。

## References
- [`WKUIDelegatePrivate.h#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L150)
- [`UIDelegate.mm#L1566`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1566)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
