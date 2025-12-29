# ``WKInternalsNotes/WKRotatingPopover/dismissionDelegate``

ポップオーバーの非表示通知を受け取るデリゲート。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign) id <WKRotatingPopoverDelegate> dismissionDelegate;
```

## Default Value
`nil`。

## Discussion
`popoverControllerDidDismissPopover:` で回転中でなければ `popoverWasDismissed:` を呼び出す。

## References
- [`WKFormPopover.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L46)
- [`WKFormPopover.mm#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L158)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
