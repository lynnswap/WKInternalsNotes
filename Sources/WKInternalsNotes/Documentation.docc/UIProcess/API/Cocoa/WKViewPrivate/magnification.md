# ``WKInternalsNotes/WKView/magnification``

拡大率を返す。

## Objective-C Declaration
```objective-c
@property (readwrite) double magnification;
```

## Default Value
`0`。

## Discussion
getter は `0` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L66)
- [`WKView.mm#L1290`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1290)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
