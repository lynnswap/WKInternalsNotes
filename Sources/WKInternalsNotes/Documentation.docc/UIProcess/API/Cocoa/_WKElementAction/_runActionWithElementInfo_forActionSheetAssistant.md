# ``WKInternalsNotes/_WKElementAction/_runActionWithElementInfo(_:forActionSheetAssistant:)``

指定のアシスタントでアクションを実行する。

## Objective-C Declaration
```objective-c
- (void)_runActionWithElementInfo:(_WKActivatedElementInfo *)info forActionSheetAssistant:(WKActionSheetAssistant *)assistant;
```

## Discussion
内部の `_actionHandler` を `assistant` と `info` で呼び出す。

## References
- [`_WKElementActionInternal.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementActionInternal.h#L40)
- [`_WKElementAction.mm#L267`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L267)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
