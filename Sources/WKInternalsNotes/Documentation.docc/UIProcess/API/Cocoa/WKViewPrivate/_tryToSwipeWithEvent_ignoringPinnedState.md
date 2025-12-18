# ``WKInternalsNotes/WKView/_tryToSwipeWithEvent(_:ignoringPinnedState:)``

スワイプ操作を試行する。

## Objective-C Declaration
```objective-c
- (BOOL)_tryToSwipeWithEvent:(NSEvent *)event ignoringPinnedState:(BOOL)ignoringPinnedState;
```

## Discussion
WKView では常に `NO` を返す。

## References
- [`WKViewPrivate.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L115)
- [`WKView.mm#L1303`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1303)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
