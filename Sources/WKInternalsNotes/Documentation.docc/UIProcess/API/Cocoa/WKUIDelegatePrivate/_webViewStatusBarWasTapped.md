# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewStatusBarWasTapped(_:)``

ステータスバータップを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewStatusBarWasTapped:(WKWebView *)webView;
```

## Discussion
UIDelegate::UIClient が status bar タップ時に delegate へ通知する。

## References
- [`WKUIDelegatePrivate.h#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L236)
- [`UIDelegate.mm#L1681`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1681)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
