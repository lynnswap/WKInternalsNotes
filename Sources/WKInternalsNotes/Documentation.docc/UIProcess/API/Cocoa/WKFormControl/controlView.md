# ``WKInternalsNotes/WKFormControl/controlView()``

フォーム制御の表示に使うビューを返す。

## Objective-C Declaration
```objective-c
- (UIView *)controlView;
```

## Discussion
`WKFormPeripheralBase` の `assistantView` が `controlView` をそのまま返し、フォーム周辺の補助ビューとして利用する。

## References
- [`WKFormPeripheral.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L41)
- [`WKFormPeripheralBase.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L75)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
