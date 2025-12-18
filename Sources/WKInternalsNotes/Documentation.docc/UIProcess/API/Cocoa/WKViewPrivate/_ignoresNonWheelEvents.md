# ``WKInternalsNotes/WKView/_ignoresNonWheelEvents``

ホイール以外のイベントを無視するか返す。

## Objective-C Declaration
```objective-c
@property (readwrite, setter=_setIgnoresNonWheelEvents:) BOOL _ignoresNonWheelEvents;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L67)
- [`WKView.mm#L1173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1173)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
