# ``WKInternalsNotes/_WKElementAction/_elementActionWithType(_:info:assistant:)``

要素情報に応じたアクションを生成する。

## Objective-C Declaration
```objective-c
+ (instancetype)_elementActionWithType:(_WKElementActionType)type info:(_WKActivatedElementInfo *)info assistant:(WKActionSheetAssistant *)assistant;
```

## Discussion
`disabled:NO` で `_elementActionWithType:info:assistant:disabled:` に委譲する。

## References
- [`_WKElementActionInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementActionInternal.h#L37)
- [`_WKElementAction.mm#L239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L239)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
