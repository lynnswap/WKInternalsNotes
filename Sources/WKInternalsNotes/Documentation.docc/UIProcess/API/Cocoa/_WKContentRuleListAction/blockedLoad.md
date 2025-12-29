# ``WKInternalsNotes/_WKContentRuleListAction/blockedLoad``

読み込みがブロックされたかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL blockedLoad;
```

## Default Value
`ENABLE(CONTENT_EXTENSIONS)` なら `_action->blockedLoad()`、無効時は `NO`。

## Discussion
`CONTENT_EXTENSIONS` 有効時は内部の `_action` を参照し、無効時は `NO` を返す。

## References
- [`_WKContentRuleListAction.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.h#L32)
- [`_WKContentRuleListAction.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.mm#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
