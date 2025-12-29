# ``WKInternalsNotes/_WKTouchEventGenerator/moveToPoint(_:duration:window:)``

単一タッチの移動イベントを送出する（内部）。

## Objective-C Declaration
```objective-c
- (void)moveToPoint:(CGPoint)location duration:(NSTimeInterval)seconds window:(UIWindow *)window;
```

## Discussion
`location` を 1 点配列にし、`moveToPoints:touchCount:duration:window:` を呼ぶ。

## References
- [`_WKTouchEventGeneratorInternal.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGeneratorInternal.h#L36)
- [`_WKTouchEventGenerator.mm#L365`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L365)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
