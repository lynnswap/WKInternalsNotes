# ``WKInternalsNotes/WKView/allowsLinkPreview()``

リンクプレビューを許可するか返す。

## Objective-C Declaration
```objective-c
- (BOOL)allowsLinkPreview;
```

## Discussion
WKView では `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L106)
- [`WKView.mm#L1151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1151)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
