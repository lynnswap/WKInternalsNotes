# ``WKInternalsNotes/WKEditorUndoTarget/undoEditing(_:)``

`WKEditCommand` の undo を実行する。

## Objective-C Declaration
```objective-c
- (void)undoEditing:(id)sender;
```

## Discussion
`sender` が `WKEditCommand` であることを確認し、`WebEditCommandProxy::unapply()` を呼ぶ。

## References
- [`WKEditCommand.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.h#L44)
- [`WKEditCommand.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
