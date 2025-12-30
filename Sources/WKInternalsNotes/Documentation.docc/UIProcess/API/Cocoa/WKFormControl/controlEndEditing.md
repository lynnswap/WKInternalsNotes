# ``WKInternalsNotes/WKFormControl/controlEndEditing()``

編集終了時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)controlEndEditing;
```

## Discussion
`WKFormPeripheralBase` が編集終了時に呼び出し、フォーム制御側が後片付けやUIの破棄を行う。

## References
- [`WKFormPeripheral.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L44)
- [`WKFormPeripheralBase.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
