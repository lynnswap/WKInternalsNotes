# ``WKInternalsNotes/WKView/shouldExpandToViewHeightForAutoLayout``

Auto Layout で高さを拡張するか返す。

## Objective-C Declaration
```objective-c
@property (readwrite) BOOL shouldExpandToViewHeightForAutoLayout;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L63)
- [`WKView.mm#L1065`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1065)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
