# ``WKInternalsNotes/WKPasswordView/hide()``

パスワード入力ビューを非表示にする。

## Objective-C Declaration
```objective-c
- (void)hide;
```

## Discussion
`showInScrollView:` で退避したズームスケール、コンテンツサイズ、背景色を元に戻し、スクロールビュー参照を破棄してビューを取り除く。

## References
- [`WKPasswordView.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.h#L34)
- [`WKPasswordView.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L109)
- [`WKPasswordView.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L111)
- [`WKPasswordView.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L117)
- [`WKPasswordView.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L120)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
