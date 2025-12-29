# ``WKInternalsNotes/WKFullScreenWindowController/initWithWebView(_:)``

`WKWebView` を関連付け、通知登録やログ設定を行う。

## Objective-C Declaration
```objective-c
- (id)initWithWebView:(WKWebView *)webView;
```

## Discussion
`self._webView` を設定し、`WebPageProxy` が取得できる場合は `logger` と `logIdentifier` を引き継ぐ。`UIApplicationDidBecomeActive` を監視し、visionOS ではベスト動画のモデルクライアントを自分に紐づける。

## References
- [`WKFullScreenWindowControllerIOS.mm#L868`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L868)
- [`WKFullScreenWindowControllerIOS.mm#L873`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L873)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
