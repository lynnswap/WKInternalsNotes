# ``WKInternalsNotes/WKRotatingPopover/dismissPopoverAnimated(_:)``

ポップオーバーを閉じる。

## Objective-C Declaration
```objective-c
- (void)dismissPopoverAnimated:(BOOL)animated;
```

## Discussion
Mac Catalyst ではフォーカス引き渡しを停止し、`UIPopoverController` を指定のアニメーション設定で閉じる。

## References
- [`WKFormPopover.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L37)
- [`WKFormPopover.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L136)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
