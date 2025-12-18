# ``WKInternalsNotes/WKView/_layoutMode``

レイアウトモードを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLayoutMode:) WKLayoutMode _layoutMode;
```

## Default Value
`0`。

## Discussion
getter は `0` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L75)
- [`WKView.mm#L1192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1192)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
