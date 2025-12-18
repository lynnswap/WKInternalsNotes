# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:willCloseLocalInspector:)``

ローカルインスペクタの終了前を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willCloseLocalInspector:(_WKInspector *)inspector WK_API_AVAILABLE(macos(12.0));
```

## Discussion
UIDelegate::UIClient が `_WKInspector` を渡し、閉じる直前の通知として呼び出す。

## References
- [`WKUIDelegatePrivate.h#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L354)
- [`UIDelegate.mm#L1247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1247)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
