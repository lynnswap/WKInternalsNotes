# ``WKInternalsNotes/WKSelectPopover/_userActionDismissedPopover(_:)``

ユーザー操作によるポップオーバー終了を通知する。

## Objective-C Declaration
```objective-c
- (void)_userActionDismissedPopover:(id)sender;
```

## Discussion
`accessoryDone` を呼んで編集終了を伝える。

## References
- [`WKFormSelectPopover.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPopover.h#L36)
- [`WKFormSelectPopover.mm#L439`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPopover.mm#L439)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
