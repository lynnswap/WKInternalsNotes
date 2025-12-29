# ``WKInternalsNotes/_WKContentRuleListAction/redirected``

リダイレクトが行われたかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL redirected WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
`ENABLE(CONTENT_EXTENSIONS)` なら `_action->redirected()`、無効時は `NO`。

## Discussion
`CONTENT_EXTENSIONS` 有効時は内部の `_action` を参照し、無効時は `NO` を返す。

## References
- [`_WKContentRuleListAction.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.h#L35)
- [`_WKContentRuleListAction.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
