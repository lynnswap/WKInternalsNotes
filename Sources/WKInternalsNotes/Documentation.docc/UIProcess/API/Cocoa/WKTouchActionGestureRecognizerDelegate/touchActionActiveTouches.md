# ``WKInternalsNotes/WKTouchActionGestureRecognizerDelegate/touchActionActiveTouches()``

touch-action のアクティブタッチを返す。

## Objective-C Declaration
```objective-c
- (NSMapTable<NSNumber *, UITouch *> *)touchActionActiveTouches;
```

## Discussion
`_touchEventGestureRecognizer` の `activeTouchesByIdentifier` を返す。

## References
- [`WKTouchActionGestureRecognizer.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.h#L44)
- [`WKContentViewInteraction.mm#L2383`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2383)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
