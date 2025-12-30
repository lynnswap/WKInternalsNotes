# ``WKInternalsNotes/WKFormControl/controlBeginEditing()``

編集開始時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)controlBeginEditing;
```

## Discussion
`WKFormPeripheralBase` が編集開始時に呼び出し、ここで各フォーム制御が必要なUI表示や準備を行う。

## References
- [`WKFormPeripheral.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L42)
- [`WKFormPeripheralBase.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
