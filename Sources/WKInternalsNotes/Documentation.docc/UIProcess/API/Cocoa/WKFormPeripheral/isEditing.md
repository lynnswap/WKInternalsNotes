# ``WKInternalsNotes/WKFormPeripheral/isEditing()``

編集状態かどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)isEditing;
```

## Discussion
`WKFormPeripheralBase` では `_editing` フラグを参照し、`beginEditing`/`endEditing` で更新される。

## References
- [`WKFormPeripheral.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L30)
- [`WKFormPeripheralBase.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
