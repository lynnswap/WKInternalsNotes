# ``WKInternalsNotes/WKTouchActionGestureRecognizer/initWithTouchActionDelegate(_:)``

デリゲートを指定して初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithTouchActionDelegate:(id <WKTouchActionGestureRecognizerDelegate>)touchActionDelegate;
```

## Discussion
`[super init]` が成功した場合に `_touchActionDelegate` を保持して返す。

## References
- [`WKTouchActionGestureRecognizer.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.h#L35)
- [`WKTouchActionGestureRecognizer.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
