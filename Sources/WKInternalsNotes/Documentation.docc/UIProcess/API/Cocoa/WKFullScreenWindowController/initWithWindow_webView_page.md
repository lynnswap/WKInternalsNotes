# ``WKInternalsNotes/WKFullScreenWindowController/initWithWindow(_:webView:page:)``

フルスクリーン用 `NSWindow` の初期設定とビュー階層の準備を行う。

## Objective-C Declaration
```objective-c
- (instancetype)initWithWindow:(NSWindow *)window webView:(WKWebView *)webView page:(std::reference_wrapper<WebKit::WebPageProxy>)page;
```

## Discussion
ウィンドウの delegate と collection behavior を設定し、タイトルバーを非表示にしてアニメーションを無効化する。背景ビューとクリップビューを作成してコンテンツビューに追加し、`_webView`/`_page` を保持する。ログ情報を引き継いだ後、`videoControlsManagerDidChange` を呼んで初期状態を整える。

## References
- [`WKFullScreenWindowController.mm#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L228)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
