# ``WKInternalsNotes/WKView/_inspectorAttachmentView``

Inspector の付属ビューを返す。

## Objective-C Declaration
```objective-c
@property (strong, nonatomic, setter=_setInspectorAttachmentView:) NSView *_inspectorAttachmentView WK_API_AVAILABLE(macos(10.11));
```

## Default Value
`nil`。

## Discussion
getter は `nil` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L89)
- [`WKView.mm#L1092`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1092)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
