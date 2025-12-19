# ``WKInternalsNotes/WKContentView/_mayDisableDoubleTapGesturesDuringSingleTap()``

シングルタップ中にダブルタップを無効化できるかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_mayDisableDoubleTapGesturesDuringSingleTap;
```

## Discussion
潜在タップ処理中 (`_potentialTapInProgress`) なら `YES`。

## References
- [`WKContentViewInteraction.h#L805`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L805)
- [`WKContentViewInteraction.mm#L2694`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2694)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
