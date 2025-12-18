# ``WKInternalsNotes/WKView/minimumSizeForAutoLayout``

Auto Layout の最小サイズを返す。

## Objective-C Declaration
```objective-c
@property (readwrite) NSSize minimumSizeForAutoLayout;
```

## Default Value
`NSZeroSize`。

## Discussion
getter は `{ }` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L60)
- [`WKView.mm#L1047`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1047)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
