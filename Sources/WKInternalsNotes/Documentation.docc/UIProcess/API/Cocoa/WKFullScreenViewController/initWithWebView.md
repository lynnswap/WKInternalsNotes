# ``WKInternalsNotes/WKFullScreenViewController/initWithWebView(_:)``

指定した `WKWebView` を使ってフルスクリーン用に初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithWebView:(WKWebView *)webView;
```

## Discussion
ステータスバーの高さ取得と通知登録、セキュリティヒューリスティックの初期化、`_webView` の設定、各種フラグ初期化を行う。

## References
- [`WKFullScreenViewController.mm#L197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L197)
- [`WKFullScreenViewController.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
