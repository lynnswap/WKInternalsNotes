# ``WKInternalsNotes/WKView/isDeferringViewInWindowChanges()``

viewInWindow 変更を遅延中か返す。

## Objective-C Declaration
```objective-c
- (BOOL)isDeferringViewInWindowChanges;
```

## Discussion
WKView では `NO` を返す。

## References
- [`WKViewPrivate.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L97)
- [`WKView.mm#L1128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
