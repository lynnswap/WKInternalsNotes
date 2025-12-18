# ``WKInternalsNotes/WKView/pageRef``

内部 WKPageRef を返す。

## Objective-C Declaration
```objective-c
@property (readonly) WKPageRef pageRef;
```

## Default Value
`nullptr`。

## Discussion
WKView では `nullptr` を返す。

## References
- [`WKViewPrivate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L39)
- [`WKView.mm#L1011`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1011)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
