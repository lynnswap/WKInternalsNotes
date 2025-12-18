# ``WKInternalsNotes/WKView/_immediateActionAnimationControllerForHitTestResult(_:withType:userData:)``

即時アクションのアニメーションコントローラを返す。

## Objective-C Declaration
```objective-c
- (id)_immediateActionAnimationControllerForHitTestResult:(WKHitTestResultRef)hitTestResult withType:(uint32_t)type userData:(WKTypeRef)userData;
```

## Discussion
WKView では `nil` を返す。

## References
- [`WKViewPrivate.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L121)
- [`WKView.mm#L1312`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1312)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
