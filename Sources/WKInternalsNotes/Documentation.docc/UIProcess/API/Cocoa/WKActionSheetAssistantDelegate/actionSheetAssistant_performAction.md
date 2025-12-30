# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:performAction:)``

指定のシートアクションを実行する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant performAction:(WebKit::SheetAction)action;
```

## Discussion
`Copy` アクションでプラグイン内リンクのコピーに成功した場合は終了する。そうでなければ `_page->performActionOnElement` でアクションを実行する。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L9992`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9992)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
