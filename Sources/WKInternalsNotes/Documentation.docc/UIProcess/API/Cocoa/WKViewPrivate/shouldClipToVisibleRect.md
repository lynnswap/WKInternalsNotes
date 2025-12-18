# ``WKInternalsNotes/WKView/shouldClipToVisibleRect``

表示領域にクリップするか返す。

## Objective-C Declaration
```objective-c
@property (readwrite) BOOL shouldClipToVisibleRect;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L62)
- [`WKView.mm#L1074`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1074)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
