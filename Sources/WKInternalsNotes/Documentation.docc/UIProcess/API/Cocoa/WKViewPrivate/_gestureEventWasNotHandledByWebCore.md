# ``WKInternalsNotes/WKView/_gestureEventWasNotHandledByWebCore(_:)``

WebCore が処理しなかったジェスチャを通知する。

## Objective-C Declaration
```objective-c
- (void)_gestureEventWasNotHandledByWebCore:(NSEvent *)event;
```

## Discussion
WKView では空実装。

## References
- [`WKViewPrivate.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L132)
- [`WKView.mm#L1270`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1270)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
