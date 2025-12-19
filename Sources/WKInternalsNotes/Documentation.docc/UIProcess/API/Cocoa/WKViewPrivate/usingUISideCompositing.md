# ``WKInternalsNotes/WKView/usingUISideCompositing``

UI side compositing を使用中か返す。

## Objective-C Declaration
```objective-c
@property (readonly, getter=isUsingUISideCompositing) BOOL usingUISideCompositing;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返す。

## References
- [`WKViewPrivate.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L64)
- [`WKView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
