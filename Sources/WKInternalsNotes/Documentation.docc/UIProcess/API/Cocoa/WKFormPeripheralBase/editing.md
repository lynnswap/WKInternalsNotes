# ``WKInternalsNotes/WKFormPeripheralBase/editing``

編集状態かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isEditing) BOOL editing;
```

## Default Value
`NO`。

## Discussion
`beginEditing`/`endEditing` で更新される `_editing` の状態を示す。

## References
- [`WKFormPeripheralBase.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L49)
- [`WKFormPeripheralBase.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L66)
- [`WKFormPeripheralBase.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
