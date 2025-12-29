# ``WKInternalsNotes/WKExtrinsicButtonDelegate/wkExtrinsicButtonWillDisplayMenu(_:)``

コンテキストメニューの表示開始を通知する。

## Objective-C Declaration
```objective-c
- (void)wkExtrinsicButtonWillDisplayMenu:(WKExtrinsicButton *)button;
```

## Discussion
`UIContextMenuInteraction` の `willDisplayMenuForConfiguration` から呼ばれる（watchOS では未実装）。

## References
- [`WKExtrinsicButton.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.mm#L45)
- [`WKExtrinsicButton.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.h#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
