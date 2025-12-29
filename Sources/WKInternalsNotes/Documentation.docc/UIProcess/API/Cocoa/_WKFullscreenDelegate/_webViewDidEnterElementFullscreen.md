# ``WKInternalsNotes/_WKFullscreenDelegate/_webViewDidEnterElementFullscreen(_:)``

要素のフルスクリーン突入を通知する（iOS）。

## Objective-C Declaration
```objective-c
- (void)_webViewDidEnterElementFullscreen:(WKWebView *)webView;
```

## Discussion
`FullscreenClient::didEnterFullscreen` から呼び出され、`_webViewDidEnterElementFullscreen:` を実装しているデリゲートに通知する。

## References
- [`_WKFullscreenDelegate.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L40)
- [`FullscreenClient.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
