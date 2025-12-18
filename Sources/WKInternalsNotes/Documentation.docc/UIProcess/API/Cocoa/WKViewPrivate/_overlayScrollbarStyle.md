# ``WKInternalsNotes/WKView/_overlayScrollbarStyle``

オーバーレイスクロールバーのスタイルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOverlayScrollbarStyle:) _WKOverlayScrollbarStyle _overlayScrollbarStyle;
```

## Default Value
`_WKOverlayScrollbarStyleDefault`。

## Discussion
getter はデフォルトを返し、setter は空実装。

## References
- [`WKViewPrivate.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L73)
- [`WKView.mm#L1241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1241)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
