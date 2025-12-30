# ``WKInternalsNotes/WKFormPeripheral/endEditing()``

編集終了処理を行う。

## Objective-C Declaration
```objective-c
- (void)endEditing;
```

## Discussion
`WKFormPeripheralBase` では編集中のみ `_editing = NO` とし、`controlEndEditing` を呼ぶ。

## References
- [`WKFormPeripheral.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L33)
- [`WKFormPeripheralBase.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
