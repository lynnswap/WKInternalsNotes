# ``WKInternalsNotes/WKFullScreenWindowController/webViewPlaceholder``

フルスクリーン遷移中に WebView を差し替えるためのプレースホルダを返す。

## Objective-C Declaration
```objective-c
@property (readonly, retain, nonatomic) UIView *webViewPlaceholder;
```

## Default Value
初期値は `nil`。フルスクリーン開始時に生成され、終了時に破棄される。

## Discussion
mac 版は `WebCoreFullScreenPlaceholderView`、iOS 版は `UIView` を返す。どちらも入場処理で生成され、WebView を一時的に置き換えるためのコンテナとして使われる。

## References
- [`WKFullScreenWindowController.mm#L302`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L302)
- [`WKFullScreenWindowController.mm#L413`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L413)
- [`WKFullScreenWindowControllerIOS.mm#L909`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L909)
- [`WKFullScreenWindowControllerIOS.mm#L1133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1133)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
