# ``WKInternalsNotes/WKView/canChangeFrameLayout(_:)``

指定フレームのレイアウト変更可否を返す。

## Objective-C Declaration
```objective-c
- (BOOL)canChangeFrameLayout:(WKFrameRef)frameRef;
```

## Discussion
WKView では `NO` を返す。

## References
- [`WKViewPrivate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L46)
- [`WKView.mm#L1016`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1016)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
