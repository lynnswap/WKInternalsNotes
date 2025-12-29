# ``WKInternalsNotes/WKContactPicker/dismissIfNeededWithReason(_:)``

終了理由に応じてピッカーを閉じる。

## Objective-C Declaration
```objective-c
- (BOOL)dismissIfNeededWithReason:(WebKit::PickerDismissalReason)reason;
```

## Discussion
`ViewRemoved` でフルスクリーン提示中の場合は閉じずに `NO` を返す。`ProcessExited` または `ViewRemoved` の場合は `delegate` を解除し、`dismiss` を呼んで `YES` を返す。

## References
- [`WKContactPicker.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.h#L51)
- [`WKContactPicker.mm#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.mm#L190)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
