# ``WKInternalsNotes/WKContentView/setSelectedColorForColorPicker(_:)``

カラーピッカーに選択色を反映する。

## Objective-C Declaration
```objective-c
- (void)setSelectedColorForColorPicker:(UIColor *)color;
```

## Discussion
`_inputPeripheral` が `WKFormColorControl` の場合に `selectColor:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L1035`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1035)
- [`WKContentViewInteraction.mm#L14513`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14513)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
