# ``WKInternalsNotes/_WKTouchEventGenerator/liftUp(_:window:)``

単一タッチの終了イベントを送出する（内部）。

## Objective-C Declaration
```objective-c
- (void)liftUp:(CGPoint)location window:(UIWindow *)window;
```

## Discussion
`touchCount` を 1 にして `liftUp:touchCount:window:` を呼び出す。

## References
- [`_WKTouchEventGeneratorInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGeneratorInternal.h#L35)
- [`_WKTouchEventGenerator.mm#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L354)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
