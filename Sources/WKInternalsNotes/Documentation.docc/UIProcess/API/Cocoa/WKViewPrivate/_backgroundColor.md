# ``WKInternalsNotes/WKView/_backgroundColor``

背景色を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setBackgroundColor:) NSColor *_backgroundColor WK_API_AVAILABLE(macos(10.14));
```

## Default Value
`nil`。

## Discussion
getter は `nil` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L87)
- [`WKView.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L100)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
