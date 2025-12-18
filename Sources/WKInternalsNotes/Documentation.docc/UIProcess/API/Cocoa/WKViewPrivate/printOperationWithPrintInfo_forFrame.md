# ``WKInternalsNotes/WKView/printOperationWithPrintInfo(_:forFrame:)``

印刷操作を生成する。

## Objective-C Declaration
```objective-c
- (NSPrintOperation *)printOperationWithPrintInfo:(NSPrintInfo *)printInfo forFrame:(WKFrameRef)frameRef;
```

## Discussion
WKView では `nil` を返す。

## References
- [`WKViewPrivate.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L45)
- [`WKView.mm#L1021`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1021)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
