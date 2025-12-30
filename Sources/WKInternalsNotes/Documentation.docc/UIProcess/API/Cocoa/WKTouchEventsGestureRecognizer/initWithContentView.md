# ``WKInternalsNotes/WKTouchEventsGestureRecognizer/initWithContentView(_:)``

`contentView` を保持し、内部状態を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithContentView:(WKContentView *)view;
```

## Discussion
`[super initWithTarget:nil action:nil]` で初期化し、`_activeTouchesByIdentifier` を `NSMapTable.strongToWeakObjectsMapTable` で生成する。`_contentView` に `view` を保持して `reset` を呼び、`self` を返す。

## References
- [`WKTouchEventsGestureRecognizer.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.h#L69)
- [`WKTouchEventsGestureRecognizer.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
