# ``WKInternalsNotes/WKFormPeripheral/beginEditing()``

編集開始処理を行う。

## Objective-C Declaration
```objective-c
- (void)beginEditing;
```

## Discussion
`WKFormPeripheralBase` では未編集時に `_editing = YES` とし、`controlBeginEditing` を呼び出す。

## References
- [`WKFormPeripheral.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L31)
- [`WKFormPeripheralBase.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
