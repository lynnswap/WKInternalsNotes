# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:gamepadsConnectedStateDidChange:)``

ゲームパッド接続状態の変化を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView gamepadsConnectedStateDidChange:(BOOL)gamepadsConnected WK_API_AVAILABLE(visionos(2.0));
```

## Discussion
visionOS で明示的な同意が必要な構成のとき、`_gamepadsConnectedStateChanged` から `_page->gamepadsConnected()` を通知する。

## References
- [`WKUIDelegatePrivate.h#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L207)
- [`WKWebView.mm#L2953`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2953)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
