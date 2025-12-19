# ``WKInternalsNotes/WKTextInteractionWrapper/selectionChangedWithTouchAt(_:withSelectionTouch:withFlags:)``

タッチ起因の選択境界変更を通知する。

## Objective-C Declaration
```objective-c
- (void)selectionChangedWithTouchAt:(CGPoint)point withSelectionTouch:(WKBESelectionTouchPhase)touch withFlags:(WKBESelectionFlags)flags;
```

## Discussion
`UIWKTextInteractionAssistant` に通知し、`USE(BROWSERENGINEKIT)` の場合は `selectionBoundaryAdjustedToPoint` を呼ぶ。

## References
- [`WKTextInteractionWrapper.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L47)
- [`WKTextInteractionWrapper.mm#L403`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L403)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
