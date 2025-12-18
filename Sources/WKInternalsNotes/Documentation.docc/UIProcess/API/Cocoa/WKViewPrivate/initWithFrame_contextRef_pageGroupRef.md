# ``WKInternalsNotes/WKView/initWithFrame(_:contextRef:pageGroupRef:)``

context/page group を指定して WKView を初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithFrame:(NSRect)frame contextRef:(WKContextRef)contextRef pageGroupRef:(WKPageGroupRef)pageGroupRef;
```

## Discussion
WKView では `nil` を返す。

## References
- [`WKViewPrivate.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L41)
- [`WKView.mm#L987`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L987)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
