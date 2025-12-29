# ``WKInternalsNotes/_WKContentRuleListAction/blockedCookies``

Cookie がブロックされたかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL blockedCookies;
```

## Default Value
`ENABLE(CONTENT_EXTENSIONS)` なら `_action->blockedCookies()`、無効時は `NO`。

## Discussion
`CONTENT_EXTENSIONS` 有効時は内部の `_action` を参照し、無効時は `NO` を返す。

## References
- [`_WKContentRuleListAction.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.h#L33)
- [`_WKContentRuleListAction.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.mm#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
