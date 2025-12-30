# ``WKInternalsNotes/_WKElementAction/runActionWithElementInfo(_:)``

既定のアクションシートアシスタントで実行する。

## Objective-C Declaration
```objective-c
- (void)runActionWithElementInfo:(_WKActivatedElementInfo *)info WK_API_AVAILABLE(macos(10.15), ios(9.0));
```

## Discussion
`_defaultActionSheetAssistant` を渡して `_runActionWithElementInfo:forActionSheetAssistant:` を呼び出す。

## References
- [`_WKElementAction.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L78)
- [`_WKElementAction.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
