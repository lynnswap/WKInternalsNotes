# ``WKInternalsNotes/WKFormPeripheral/handleKeyEvent(_:)``

キーイベントを処理する。

## Objective-C Declaration
```objective-c
- (BOOL)handleKeyEvent:(UIEvent *)event;
```

## Discussion
`WKFormPeripheralBase` では `controlHandleKeyEvent:` があれば委譲し、未処理ならキー状態を判定する。Escape で `accessoryDone`、Spacebar で `accessoryOpen` を呼ぶ。

## References
- [`WKFormPeripheral.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L36)
- [`WKFormPeripheralBase.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L85)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
