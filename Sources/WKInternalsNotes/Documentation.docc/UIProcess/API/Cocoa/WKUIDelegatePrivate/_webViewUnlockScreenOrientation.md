# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewUnlockScreenOrientation(_:)``

画面回転ロック解除を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewUnlockScreenOrientation:(WKWebView *)webView WK_API_AVAILABLE(ios(16.4));
```

## Discussion
UIDelegate::UIClient が delegate を通じて画面回転ロック解除を依頼する。

## References
- [`WKUIDelegatePrivate.h#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L292)
- [`UIDelegate.mm#L759`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L759)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
