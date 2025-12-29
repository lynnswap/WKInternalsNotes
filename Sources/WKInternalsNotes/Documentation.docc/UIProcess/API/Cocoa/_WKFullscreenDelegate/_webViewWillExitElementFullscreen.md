# ``WKInternalsNotes/_WKFullscreenDelegate/_webViewWillExitElementFullscreen(_:)``

要素フルスクリーン終了直前を通知する（iOS）。

## Objective-C Declaration
```objective-c
- (void)_webViewWillExitElementFullscreen:(WKWebView *)webView;
```

## Discussion
`FullscreenClient::willExitFullscreen` から呼び出され、`_webViewWillExitElementFullscreen:` を実装しているデリゲートに通知する。

## References
- [`_WKFullscreenDelegate.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L41)
- [`FullscreenClient.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
