# ``WKInternalsNotes/WKContentView/toolTipInteraction(_:configurationAtPoint:)``

ツールチップ表示設定を返す。

## Objective-C Declaration
```objective-c
- (UIToolTipConfiguration *)toolTipInteraction:(UIToolTipInteraction *)interaction configurationAtPoint:(CGPoint)point;
```

## Discussion
`interaction.defaultToolTip` を用いた `UIToolTipConfiguration` を返す。

## References
- [`WKContentViewInteraction.h#L889`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L889)
- [`WKContentViewInteraction.mm#L11541`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11541)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
