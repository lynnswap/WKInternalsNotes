# ``WKInternalsNotes/WKView/_setDidMoveSwipeSnapshotCallback(_:)``

スワイプスナップショット移動時のコールバックを設定する。

## Objective-C Declaration
```objective-c
- (void)_setDidMoveSwipeSnapshotCallback:(void(^)(CGRect swipeSnapshotRectInWindowCoordinates))callback;
```

## Discussion
WKView では空実装。

## References
- [`WKViewPrivate.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L117)
- [`WKView.mm#L1308`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1308)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
