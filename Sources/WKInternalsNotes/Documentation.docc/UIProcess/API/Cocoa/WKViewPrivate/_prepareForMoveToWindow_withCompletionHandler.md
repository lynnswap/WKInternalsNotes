# ``WKInternalsNotes/WKView/_prepareForMoveToWindow(_:withCompletionHandler:)``

ウィンドウ移動前の準備を行う。

## Objective-C Declaration
```objective-c
- (void)_prepareForMoveToWindow:(NSWindow *)targetWindow withCompletionHandler:(void(^)(void))completionHandler;
```

## Discussion
WKView では空実装で、completion handler は呼ばれない。

## References
- [`WKViewPrivate.h#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L98)
- [`WKView.mm#L1124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1124)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
