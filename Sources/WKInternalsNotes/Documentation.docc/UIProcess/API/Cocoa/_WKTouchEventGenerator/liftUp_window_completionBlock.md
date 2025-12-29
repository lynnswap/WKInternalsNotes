# ``WKInternalsNotes/_WKTouchEventGenerator/liftUp(_:window:completionBlock:)``

タッチ終了イベントを送出し、完了コールバックを登録する。

## Objective-C Declaration
```objective-c
- (void)liftUp:(CGPoint)location window:(UIWindow *)window completionBlock:(void (^)(void))completionBlock;
```

## Discussion
内部の `liftUp:window:` を呼んだ後、マーカー HID イベントを送出して `completionBlock` を紐づける。

## References
- [`_WKTouchEventGenerator.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.h#L42)
- [`_WKTouchEventGenerator.mm#L359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L359)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
