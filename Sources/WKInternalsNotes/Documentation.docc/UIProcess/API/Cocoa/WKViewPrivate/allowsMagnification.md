# ``WKInternalsNotes/WKView/allowsMagnification``

拡大縮小を許可するか返す。

## Objective-C Declaration
```objective-c
@property (readwrite) BOOL allowsMagnification;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L65)
- [`WKView.mm#L1251`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1251)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
