# ``WKInternalsNotes/WKMouseInteraction/hasGesture(_:)``

内部で管理しているジェスチャーかどうかを判定する。

## Objective-C Declaration
```objective-c
- (BOOL)hasGesture:(UIGestureRecognizer *)gesture;
```

## Discussion
引数が `WKMouseTouchGestureRecognizer`、`_mouseHoverGestureRecognizer`、`_pencilHoverGestureRecognizer` のいずれかと一致すれば `YES`。

## References
- [`WKMouseInteraction.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L47)
- [`WKMouseInteraction.mm#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L190)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
