# ``WKInternalsNotes/WKFormControl/controlHandleKeyEvent(_:)``

キーボードイベントを処理する。

## Objective-C Declaration
```objective-c
- (BOOL)controlHandleKeyEvent:(UIEvent *)event;
```

## Discussion
`WKFormPeripheralBase` が `controlHandleKeyEvent:` に応答していれば呼び出し、`YES` ならイベントを消費する。未消費の場合は `Escape` でアクセサリ終了、`Space` でアクセサリ表示などを処理する。

## References
- [`WKFormPeripheral.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheral.h#L46)
- [`WKFormPeripheralBase.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L85)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
