# ``WKInternalsNotes/_WKFindDelegate/_webView(_:didAddLayerForFindOverlay:)``

Find オーバーレイの `CALayer` が追加された通知を受け取る。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didAddLayerForFindOverlay:(CALayer *)layer;
```

## Discussion
`WKWebView` が Find オーバーレイ用レイヤーを追加した際に `FindClient::didAddLayerForFindOverlay` から delegate に転送される。実装している場合のみ呼ばれ、引数の `layer` がそのオーバーレイのレイヤー。

## References
- [`WKWebViewIOS.mm#L4077`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4077)
- [`FindClient.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FindClient.mm#L75)
- [`_WKFindDelegate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFindDelegate.h#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
