# ``WKInternalsNotes/WKActionSheet/arrowDirections``

ポップオーバー矢印の表示方向を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) UIPopoverArrowDirection arrowDirections;
```

## Default Value
`init` で `UIPopoverArrowDirectionAny` に設定される。

## Discussion
`presentSheetFromRect:` で `permittedArrowDirections` に設定される。

## References
- [`WKActionSheet.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L43)
- [`WKActionSheet.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L47)
- [`WKActionSheet.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L53)
- [`WKActionSheet.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L120)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
