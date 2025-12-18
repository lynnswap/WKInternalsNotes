# ``WKInternalsNotes/WKView/_useSystemAppearance``

システム外観を使用するか返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setUseSystemAppearance:) BOOL _useSystemAppearance WK_API_AVAILABLE(macos(10.14));
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L144)
- [`WKView.mm#L1394`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1394)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
