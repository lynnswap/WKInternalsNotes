# ``WKInternalsNotes/_WKFullscreenDelegate/_webViewDidEnterFullscreen(_:)``

フルスクリーン突入を通知する（macOS）。

## Objective-C Declaration
```objective-c
- (void)_webViewDidEnterFullscreen:(NSView *)webView;
```

## Discussion
`FullscreenClient::didEnterFullscreen` から呼び出され、`_webViewDidEnterFullscreen:` を実装しているデリゲートに通知する。

## References
- [`_WKFullscreenDelegate.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L49)
- [`FullscreenClient.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
