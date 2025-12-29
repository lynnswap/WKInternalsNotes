# ``WKInternalsNotes/_WKTouchEventGenerator/eventCallbacks``

マーカーイベントの完了コールバック辞書。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) NSMutableDictionary *eventCallbacks;
```

## Default Value
`init` で空の `NSMutableDictionary` を生成する。

## Discussion
マーカー HID イベントの callback ID をキーに完了ブロックを保持し、`receivedHIDEvent:` で呼び出して削除する。

## References
- [`_WKTouchEventGeneratorInternal.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGeneratorInternal.h#L41)
- [`_WKTouchEventGenerator.mm#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L122)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
