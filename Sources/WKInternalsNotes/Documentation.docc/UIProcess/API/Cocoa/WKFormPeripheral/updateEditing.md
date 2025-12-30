# ``WKInternalsNotes/WKFormPeripheral/updateEditing()``

編集状態の更新処理を行う。

## Objective-C Declaration
```objective-c
- (void)updateEditing;
```

## Discussion
`WKFormPeripheralBase` では編集中のみ `controlUpdateEditing` を呼ぶ。

## References
- [`WKFormPeripheral.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L32)
- [`WKFormPeripheralBase.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
