# ``WKInternalsNotes/WKContentView/_setFontForWebView(_:sender:)``

指定フォントに合わせて文字スタイルを更新する。

## Objective-C Declaration
```objective-c
- (void)_setFontForWebView:(UIFont *)fontFamily sender:(id)sender;
```

## Discussion
`UIFont` から `FontChanges` を構築し、フォント名/サイズ/太字/斜体を設定して `changeFont` を呼び出す。

## References
- [`WKContentViewInteraction.h#L785`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L785)
- [`WKContentViewInteraction.mm#L4533`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4533)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
