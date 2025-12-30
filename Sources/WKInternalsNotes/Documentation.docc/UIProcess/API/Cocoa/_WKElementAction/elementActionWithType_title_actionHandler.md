# ``WKInternalsNotes/_WKElementAction/elementActionWithType(_:title:actionHandler:)``

タイプとタイトル、ハンドラを指定してアクションを作成する。

## Objective-C Declaration
```objective-c
+ (instancetype)elementActionWithType:(_WKElementActionType)type title:(NSString *)title actionHandler:(WKElementActionHandler)actionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
内部の `_elementActionWithType:title:actionHandler:` に委譲し、ハンドラを `WKActionSheetAssistant` 無しの形に変換して保持する。

## References
- [`_WKElementAction.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L69)
- [`_WKElementAction.mm#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L127)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
