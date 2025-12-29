# ``WKInternalsNotes/_WKTouchEventGenerator/touchDown(_:window:)``

単一タッチの開始イベントを送出する（内部）。

## Objective-C Declaration
```objective-c
- (void)touchDown:(CGPoint)location window:(UIWindow *)window;
```

## Discussion
`touchCount` を 1 にして `touchDown:touchCount:window:` を呼び出す。

## References
- [`_WKTouchEventGeneratorInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGeneratorInternal.h#L34)
- [`_WKTouchEventGenerator.mm#L343`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L343)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
