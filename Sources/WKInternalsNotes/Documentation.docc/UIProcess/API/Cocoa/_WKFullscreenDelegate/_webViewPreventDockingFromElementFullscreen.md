# ``WKInternalsNotes/_WKFullscreenDelegate/_webViewPreventDockingFromElementFullscreen(_:)``

要素フルスクリーン時のドッキング可否を返す。

## Objective-C Declaration
```objective-c
- (BOOL)_webViewPreventDockingFromElementFullscreen:(WKWebView *)webView;
```

## Discussion
`FullscreenClient::preventDocking` から呼び出され、未実装の場合は `false` が返る。

## References
- [`_WKFullscreenDelegate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L46)
- [`FullscreenClient.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
