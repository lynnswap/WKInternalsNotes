# ``WKInternalsNotes/WKFormColorControl/initWithView(_:)``

カラー選択用のフォームコントロールを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view;
```

## Discussion
`WKColorPicker` を生成し、`WKFormPeripheralBase` の `initWithView:control:` で初期化する。

## References
- [`WKFormColorControl.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormColorControl.h#L34)
- [`WKFormColorControl.mm#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormColorControl.mm#L161)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
