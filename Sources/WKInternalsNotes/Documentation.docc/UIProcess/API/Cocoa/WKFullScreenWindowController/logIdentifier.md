# ``WKInternalsNotes/WKFullScreenWindowController/logIdentifier``

ログ出力用の識別子を返す。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) uint64_t logIdentifier;
```

## Default Value
初期値は 0。初期化時に `WebPageProxy` の `logIdentifier` を保存する。

## Discussion
`_logIdentifier` を返すだけのアクセサ。mac 版は `initWithWindow:webView:page:`、iOS 版は `initWithWebView:` で `WebPageProxy` の値を取り込む。

## References
- [`WKFullScreenWindowController.mm#L1090`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L1090)
- [`WKFullScreenWindowController.mm#L263`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L263)
- [`WKFullScreenWindowControllerIOS.mm#L2289`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2289)
- [`WKFullScreenWindowControllerIOS.mm#L877`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L877)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
