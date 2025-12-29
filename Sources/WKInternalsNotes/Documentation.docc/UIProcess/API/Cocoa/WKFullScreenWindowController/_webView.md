# ``WKInternalsNotes/WKFullScreenWindowController/_webView``

フルスクリーン処理対象の `WKWebView` を弱参照で保持する。

## Objective-C Declaration
```objective-c
@property (weak, nonatomic) WKWebView *_webView;
```

## Default Value
初期値は `nil`。`initWithWebView:` で渡された `WKWebView` を設定し、weak 参照のため WebView の破棄で `nil` になる。

## Discussion
循環参照を避けるため弱参照として保持し、`_page` 取得や UI の更新などフルスクリーン処理の起点として参照される。`WKWebView` が破棄済みの場合は `nil` になるため、呼び出し側は `nil` を前提に処理を分岐する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L767`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L767)
- [`WKFullScreenWindowControllerIOS.mm#L873`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L873)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
