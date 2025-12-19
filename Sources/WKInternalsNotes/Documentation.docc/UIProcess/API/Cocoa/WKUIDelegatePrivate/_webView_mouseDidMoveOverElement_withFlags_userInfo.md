# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:mouseDidMoveOverElement:withFlags:userInfo:)``

マウス移動時のヒットテスト結果と修飾キーを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webview mouseDidMoveOverElement:(_WKHitTestResult *)hitTestResult withFlags:(UIKeyModifierFlags)flags userInfo:(id <NSSecureCoding>)userInfo WK_API_AVAILABLE(ios(16.0));
```

## Discussion
UIClient が `API::HitTestResult` を作成し、macOS では `NSEventModifierFlags`、iOS では `UIKeyModifierFlags` に変換した修飾キーを渡して通知する。`userInfo` は `nil` で渡される。

## References
- [`WKUIDelegatePrivate.h#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L233)
- [`WKUIDelegatePrivate.h#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L233)
- [`UIDelegate.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
