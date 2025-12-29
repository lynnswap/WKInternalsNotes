# ``WKInternalsNotes/_WKFullscreenDelegate/_webViewDidExitFullscreen(_:)``

フルスクリーン終了を通知する（macOS）。

## Objective-C Declaration
```objective-c
- (void)_webViewDidExitFullscreen:(NSView *)webView;
```

## Discussion
`FullscreenClient::didExitFullscreen` から呼び出され、`_webViewDidExitFullscreen:` を実装しているデリゲートに通知する。

## References
- [`_WKFullscreenDelegate.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L51)
- [`FullscreenClient.mm#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L129)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
