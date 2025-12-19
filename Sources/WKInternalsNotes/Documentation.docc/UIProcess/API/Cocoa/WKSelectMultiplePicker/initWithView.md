# ``WKInternalsNotes/WKSelectMultiplePicker/initWithView(_:)``

複数選択用のピッカーを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view;
```

## Discussion
`WKSelectPickerTableViewController` とそれを包む `UINavigationController` を生成し、関連する `WKContentView` を保持する。

## References
- [`WKFormSelectPicker.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.h#L54)
- [`WKFormSelectPicker.mm#L1242`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L1242)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
