# ``WKInternalsNotes/WKView/_ignoresAllEvents``

全イベントを無視するか返す。

## Objective-C Declaration
```objective-c
@property (readwrite, setter=_setIgnoresAllEvents:) BOOL _ignoresAllEvents;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L68)
- [`WKView.mm#L1178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1178)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
