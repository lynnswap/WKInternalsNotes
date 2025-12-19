# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:printFrame:)``

指定フレームの印刷を delegate に依頼する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView printFrame:(_WKFrameHandle *)frame;
```

## Discussion
UIDelegate::UIClient が PDF サイズ付き API 未実装時にこのメソッドを呼び、処理後に `completionHandler` を実行する。

## References
- [`WKUIDelegatePrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L141)
- [`UIDelegate.mm#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L159)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
