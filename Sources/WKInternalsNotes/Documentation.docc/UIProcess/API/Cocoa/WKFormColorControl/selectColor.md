# ``WKInternalsNotes/WKFormColorControl/selectColor(_:)``

テスト用途で色を選択する。

## Objective-C Declaration
```objective-c
- (void)selectColor:(UIColor *)color;
```

## Discussion
`self.control` が `WKColorPicker` の場合に `selectColor:` を呼び出す。

## References
- [`WKFormColorControl.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormColorControl.h#L38)
- [`WKFormColorControl.mm#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormColorControl.mm#L172)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
