# ``WKInternalsNotes/_WKContentRuleListAction/notifications``

通知名の配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSString *> *notifications;
```

## Default Value
`CONTENT_EXTENSIONS` 無効時や通知が空の場合は `nil`。

## Discussion
`CONTENT_EXTENSIONS` 有効時は `_action->notifications()` を配列化して返す。空なら `nil` を返す。

## References
- [`_WKContentRuleListAction.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.h#L37)
- [`_WKContentRuleListAction.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentRuleListAction.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
