# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistantDidDismissContextMenu(_:)``

コンテキストメニュー非表示を通知する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistantDidDismissContextMenu:(WKActionSheetAssistant *)assistant;
```

## Discussion
`[_webView _didDismissContextMenu]` を呼び、WebView 側に非表示を通知する。

## References
- [`WKActionSheetAssistant.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L80)
- [`WKContentViewInteraction.mm#L10192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10192)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
