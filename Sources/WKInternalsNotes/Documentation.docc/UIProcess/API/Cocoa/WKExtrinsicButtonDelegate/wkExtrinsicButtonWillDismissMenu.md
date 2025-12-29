# ``WKInternalsNotes/WKExtrinsicButtonDelegate/wkExtrinsicButtonWillDismissMenu(_:)``

コンテキストメニューの終了を通知する。

## Objective-C Declaration
```objective-c
- (void)wkExtrinsicButtonWillDismissMenu:(WKExtrinsicButton *)button;
```

## Discussion
`UIContextMenuInteraction` の `willEndForConfiguration` から呼ばれる（watchOS では未実装）。

## References
- [`WKExtrinsicButton.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.mm#L51)
- [`WKExtrinsicButton.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.h#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
