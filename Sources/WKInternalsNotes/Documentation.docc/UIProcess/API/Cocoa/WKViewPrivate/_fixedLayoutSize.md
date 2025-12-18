# ``WKInternalsNotes/WKView/_fixedLayoutSize``

固定レイアウト時のサイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setFixedLayoutSize:) CGSize _fixedLayoutSize;
```

## Default Value
`CGSizeZero`。

## Discussion
getter は空のサイズを返し、setter は空実装。

## References
- [`WKViewPrivate.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L77)
- [`WKView.mm#L1201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1201)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
