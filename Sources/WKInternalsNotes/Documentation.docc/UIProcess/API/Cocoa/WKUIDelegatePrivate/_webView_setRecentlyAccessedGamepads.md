# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:setRecentlyAccessedGamepads:)``

最近アクセスしたゲームパッドの状態を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView setRecentlyAccessedGamepads:(BOOL)recentlyAccessedGamepads WK_API_AVAILABLE(visionos(2.0));
```

## Discussion
visionOS で明示的な同意が必要な場合に、`_gamepadsRecentlyAccessed` の更新と合わせて delegate へ通知する。

## References
- [`WKUIDelegatePrivate.h#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L227)
- [`WKWebView.mm#L2954`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2954)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
