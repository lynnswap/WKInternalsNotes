# ``WKInternalsNotes/_WKTouchEventGenerator/moveToPoint(_:duration:window:completionBlock:)``

タッチ移動イベントを送出し、完了コールバックを登録する。

## Objective-C Declaration
```objective-c
- (void)moveToPoint:(CGPoint)location duration:(NSTimeInterval)seconds window:(UIWindow *)window completionBlock:(void (^)(void))completionBlock;
```

## Discussion
内部の `moveToPoint:duration:window:` を呼んだ後、マーカー HID イベントを送出して `completionBlock` を紐づける。

## References
- [`_WKTouchEventGenerator.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.h#L43)
- [`_WKTouchEventGenerator.mm#L372`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L372)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
