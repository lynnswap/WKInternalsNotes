# ``WKInternalsNotes/_WKFullscreenDelegate/_webViewWillExitFullscreen(_:)``

フルスクリーン終了直前を通知する（macOS）。

## Objective-C Declaration
```objective-c
- (void)_webViewWillExitFullscreen:(NSView *)webView;
```

## Discussion
`FullscreenClient::willExitFullscreen` から呼び出され、`_webViewWillExitFullscreen:` を実装しているデリゲートに通知する。

## References
- [`_WKFullscreenDelegate.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L50)
- [`FullscreenClient.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
