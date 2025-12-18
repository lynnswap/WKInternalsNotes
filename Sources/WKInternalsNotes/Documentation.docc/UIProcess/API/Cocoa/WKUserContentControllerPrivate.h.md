# ``WKInternalsNotes/WKUserContentController``

WKUserContentController の Objective-C private/testing API をカテゴリ別に整理した一覧。

## Topics

### WKPrivate

#### Properties
- ``WKInternalsNotes/WKUserContentController/_userStyleSheets``

#### Methods
- ``WKInternalsNotes/WKUserContentController/_addContentRuleList(_:extensionBaseURL:)``
- ``WKInternalsNotes/WKUserContentController/_addScriptMessageHandler(_:name:contentWorld:)``
- ``WKInternalsNotes/WKUserContentController/_addScriptMessageHandler(_:name:userContentWorld:)``
- ``WKInternalsNotes/WKUserContentController/_addUserContentFilter(_:)``
- ``WKInternalsNotes/WKUserContentController/_addUserScriptImmediately(_:)``
- ``WKInternalsNotes/WKUserContentController/_addUserStyleSheet(_:)``
- ``WKInternalsNotes/WKUserContentController/_removeAllScriptMessageHandlersAssociatedWithUserContentWorld(_:)``
- ``WKInternalsNotes/WKUserContentController/_removeAllUserContentFilters()``
- ``WKInternalsNotes/WKUserContentController/_removeAllUserScriptsAssociatedWithContentWorld(_:)``
- ``WKInternalsNotes/WKUserContentController/_removeAllUserStyleSheets()``
- ``WKInternalsNotes/WKUserContentController/_removeAllUserStyleSheetsAssociatedWithContentWorld(_:)``
- ``WKInternalsNotes/WKUserContentController/_removeScriptMessageHandlerForName(_:userContentWorld:)``
- ``WKInternalsNotes/WKUserContentController/_removeUserContentFilter(_:)``
- ``WKInternalsNotes/WKUserContentController/_removeUserScript(_:)``
- ``WKInternalsNotes/WKUserContentController/_removeUserStyleSheet(_:)``

### Class Extension

- ``WKInternalsNotes/WKUserContentController/_addScriptMessageHandler(_:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`WKUserContentControllerPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h) |
