# ``WKInternalsNotes/WKRotatingPopoverDelegate/popoverWasDismissed(_:)``

ポップオーバーが閉じられたことを通知する。

## Objective-C Declaration
```objective-c
- (void)popoverWasDismissed:(WKRotatingPopover *)popover;
```

## Discussion
`WKFormRotatingAccessoryPopover` はこの通知で `accessoryDone` を呼び出す。

## References
- [`WKFormPopover.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L51)
- [`WKFormPopover.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
