# ``WKInternalsNotes/WKTextInteractionWrapper/selectionChangedWithGestureAt(_:withGesture:withState:withFlags:)``

ジェスチャ起因の選択変更を通知する。

## Objective-C Declaration
```objective-c
- (void)selectionChangedWithGestureAt:(CGPoint)point withGesture:(WKBEGestureType)gestureType withState:(UIGestureRecognizerState)gestureState withFlags:(WKBESelectionFlags)flags;
```

## Discussion
`UIWKTextInteractionAssistant` にジェスチャ種別やフラグを変換して通知し、`USE(BROWSERENGINEKIT)` の場合は `BETextInteraction` にも同じ情報を伝える。

## References
- [`WKTextInteractionWrapper.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L46)
- [`WKTextInteractionWrapper.mm#L395`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L395)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
