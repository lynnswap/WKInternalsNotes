# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistantDidStopInteraction(_:)``

インタラクション終了を通知する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistantDidStopInteraction:(WKActionSheetAssistant *)assistant;
```

## Discussion
`_page->stopInteraction()` を呼び、インタラクションの終了を伝える。

## References
- [`WKActionSheetAssistant.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L72)
- [`WKContentViewInteraction.mm#L10094`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10094)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
