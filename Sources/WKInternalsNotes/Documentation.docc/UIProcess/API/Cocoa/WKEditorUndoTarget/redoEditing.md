# ``WKInternalsNotes/WKEditorUndoTarget/redoEditing(_:)``

`WKEditCommand` の redo を実行する。

## Objective-C Declaration
```objective-c
- (void)redoEditing:(id)sender;
```

## Discussion
`sender` が `WKEditCommand` であることを確認し、`WebEditCommandProxy::reapply()` を呼ぶ。

## References
- [`WKEditCommand.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.h#L45)
- [`WKEditCommand.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.mm#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
