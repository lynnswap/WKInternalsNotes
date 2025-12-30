# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistantDidShowContextMenu(_:)``

コンテキストメニュー表示を通知する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistantDidShowContextMenu:(WKActionSheetAssistant *)assistant;
```

## Discussion
`[_webView _didShowContextMenu]` を呼び、WebView 側に表示を通知する。

## References
- [`WKActionSheetAssistant.h#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L79)
- [`WKContentViewInteraction.mm#L10187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
