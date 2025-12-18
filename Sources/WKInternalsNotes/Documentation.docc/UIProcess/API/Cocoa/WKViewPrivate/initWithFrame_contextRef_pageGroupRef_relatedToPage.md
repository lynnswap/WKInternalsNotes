# ``WKInternalsNotes/WKView/initWithFrame(_:contextRef:pageGroupRef:relatedToPage:)``

関連ページを指定して WKView を初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithFrame:(NSRect)frame contextRef:(WKContextRef)contextRef pageGroupRef:(WKPageGroupRef)pageGroupRef relatedToPage:(WKPageRef)relatedPage;
```

## Discussion
WKView では `nil` を返す。

## References
- [`WKViewPrivate.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L42)
- [`WKView.mm#L992`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L992)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
