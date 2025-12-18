# ``WKInternalsNotes/WKView/underlayColor``

下層の色を返す。

## Objective-C Declaration
```objective-c
@property (copy, nonatomic) NSColor *underlayColor;
```

## Default Value
`nil`。

## Discussion
getter は `nil` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L85)
- [`WKView.mm#L1083`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1083)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
