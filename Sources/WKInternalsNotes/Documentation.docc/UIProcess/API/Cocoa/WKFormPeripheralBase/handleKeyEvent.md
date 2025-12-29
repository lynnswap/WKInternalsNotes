# ``WKInternalsNotes/WKFormPeripheralBase/handleKeyEvent(_:)``

キーボードイベントを処理する。

## Objective-C Declaration
```objective-c
- (BOOL)handleKeyEvent:(UIEvent *)event;
```

## Discussion
`controlHandleKeyEvent:` が実装されていれば委譲し、`YES` が返れば処理を終了する。キーアップや修飾キーのみのイベントは無視し、編集中の Escape で `accessoryDone`、非編集中の Space で `accessoryOpen` を呼び出す。

## References
- [`WKFormPeripheralBase.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L85)
- [`WKFormPeripheralBase.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
