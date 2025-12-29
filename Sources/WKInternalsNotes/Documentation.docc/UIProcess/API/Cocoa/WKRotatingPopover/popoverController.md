# ``WKInternalsNotes/WKRotatingPopover/popoverController``

表示に使う `UIPopoverController` を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, retain) UIPopoverController *popoverController;
```

## Default Value
`nil`。

## Discussion
setter では旧コントローラの delegate を解除し、新しいコントローラを設定して自身を delegate にする。

## References
- [`WKFormPopover.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L44)
- [`WKFormPopover.mm#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L98)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
