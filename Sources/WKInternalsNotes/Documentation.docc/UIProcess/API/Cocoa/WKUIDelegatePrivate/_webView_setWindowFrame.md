# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:setWindowFrame:)``

WebView のウィンドウフレーム設定を delegate に依頼する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView setWindowFrame:(CGRect)frame WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIDelegate::UIClient が `CGRect` を渡してウィンドウ位置とサイズの変更を delegate に委譲する。

## References
- [`WKUIDelegatePrivate.h#L331`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L331)
- [`UIDelegate.mm#L1130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1130)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
