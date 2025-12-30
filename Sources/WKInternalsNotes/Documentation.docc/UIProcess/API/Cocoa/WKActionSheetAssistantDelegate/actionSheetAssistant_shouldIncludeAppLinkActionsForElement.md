# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:shouldIncludeAppLinkActionsForElement:)``

App Link アクションを含めるか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)actionSheetAssistant:(WKActionSheetAssistant *)assistant shouldIncludeAppLinkActionsForElement:(_WKActivatedElementInfo *)element;
```

## Discussion
`_page->uiClient().shouldIncludeAppLinkActionsForElement(element)` の結果を返す。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L10028`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10028)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
