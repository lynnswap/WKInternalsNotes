# ``WKInternalsNotes/_WKFullscreenDelegate/_webViewWillEnterElementFullscreen(_:)``

要素フルスクリーン開始直前を通知する（iOS）。

## Objective-C Declaration
```objective-c
- (void)_webViewWillEnterElementFullscreen:(WKWebView *)webView;
```

## Discussion
`FullscreenClient::willEnterFullscreen` から呼び出され、`_webViewWillEnterElementFullscreen:` を実装しているデリゲートに通知する。

## References
- [`_WKFullscreenDelegate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L39)
- [`FullscreenClient.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
