# ``WKInternalsNotes/_WKTouchEventGenerator/receivedHIDEvent(_:)``

ベンダー定義HIDイベントのコールバックを処理する。

## Objective-C Declaration
```objective-c
- (void)receivedHIDEvent:(IOHIDEventRef)event;
```

## Discussion
ベンダー定義イベント以外は無視する。`kIOHIDEventFieldVendorDefinedData` から取得したコールバックIDで `_eventCallbacks` を引き、該当するブロックがあれば辞書から削除して実行・解放する。

## References
- [`_WKTouchEventGenerator.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.h#L47)
- [`_WKTouchEventGenerator.mm#L378`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L378)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
