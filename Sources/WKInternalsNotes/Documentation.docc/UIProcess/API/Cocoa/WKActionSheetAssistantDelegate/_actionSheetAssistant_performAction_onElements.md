# ``WKInternalsNotes/WKActionSheetAssistantDelegate/_actionSheetAssistant(_:performAction:onElements:)``

複数要素に対してアクションを実行する。

## Objective-C Declaration
```objective-c
- (void)_actionSheetAssistant:(WKActionSheetAssistant *)assistant performAction:(WebKit::SheetAction)action onElements:(Vector<WebCore::ElementContext>&&)elements;
```

## Discussion
`_page->performActionOnElements` を呼び、渡された要素集合に対してアクションを適用する。

## References
- [`WKActionSheetAssistant.h#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L95)
- [`WKContentViewInteraction.mm#L10000`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10000)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
