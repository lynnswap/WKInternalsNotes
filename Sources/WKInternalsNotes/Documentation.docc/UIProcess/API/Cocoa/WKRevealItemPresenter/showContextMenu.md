# ``WKInternalsNotes/WKRevealItemPresenter/showContextMenu()``

Reveal アイテムのコンテキストメニューを表示する。

## Objective-C Declaration
```objective-c
- (void)showContextMenu;
```

## Discussion
`WebViewImpl` と `view` が取得できる場合のみ処理を進める。`RVPresenter` からメニュー項目を取得し、空の場合は終了する。`NSMenu` を構築してクリック位置に対応する `NSEvent` を生成し、`popUpContextMenu` で表示したあと `didFinishPresentation` を通知する。

## References
- [`WKRevealItemPresenter.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.h#L42)
- [`WKRevealItemPresenter.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L67)
- [`WKRevealItemPresenter.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L69)
- [`WKRevealItemPresenter.mm#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L77)
- [`WKRevealItemPresenter.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L81)
- [`WKRevealItemPresenter.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L85)
- [`WKRevealItemPresenter.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
