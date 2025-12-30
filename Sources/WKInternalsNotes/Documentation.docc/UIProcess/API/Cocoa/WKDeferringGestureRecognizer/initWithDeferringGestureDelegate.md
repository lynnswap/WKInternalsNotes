# ``WKInternalsNotes/WKDeferringGestureRecognizer/initWithDeferringGestureDelegate(_:)``

デリゲートを指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDeferringGestureDelegate:(id <WKDeferringGestureRecognizerDelegate>)deferringGestureDelegate;
```

## Discussion
`[super init]` に成功した場合、`_deferringGestureDelegate` を設定して返す。

## References
- [`WKDeferringGestureRecognizer.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L48)
- [`WKDeferringGestureRecognizer.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.mm#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
