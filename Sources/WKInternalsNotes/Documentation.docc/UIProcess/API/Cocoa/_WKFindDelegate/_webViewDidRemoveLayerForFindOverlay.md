# ``WKInternalsNotes/_WKFindDelegate/_webViewDidRemoveLayerForFindOverlay(_:)``

Find オーバーレイのレイヤーが削除された通知を受け取る。

## Objective-C Declaration
```objective-c
- (void)_webViewDidRemoveLayerForFindOverlay:(WKWebView *)webView;
```

## Discussion
`WKWebView` の `_didRemoveLayerForFindOverlay` から `FindClient::didRemoveLayerForFindOverlay` を経由して delegate に転送される。実装している場合のみ呼ばれる。

## References
- [`WKWebViewIOS.mm#L4093`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4093)
- [`FindClient.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FindClient.mm#L81)
- [`_WKFindDelegate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFindDelegate.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
