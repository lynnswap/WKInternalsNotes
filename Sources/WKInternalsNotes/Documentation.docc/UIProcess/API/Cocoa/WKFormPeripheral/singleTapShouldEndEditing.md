# ``WKInternalsNotes/WKFormPeripheral/singleTapShouldEndEditing``

単タップで編集終了するかのフラグ。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL singleTapShouldEndEditing;
```

## Default Value
`WKFormPeripheralBase` では自動合成され、初期値は `NO`。

## Discussion
プロパティとして保持されるのみで、基底クラス側の明示的な処理はない。

## References
- [`WKFormPeripheral.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L37)
- [`WKFormPeripheralBase.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
