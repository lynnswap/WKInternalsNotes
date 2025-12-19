# ``WKInternalsNotes/WKEditCommand/command()``

内部の `WebEditCommandProxy` を返す。

## Objective-C Declaration
```objective-c
- (WebKit::WebEditCommandProxy&)command;
```

## Discussion
`_command` を参照で返し、undo/redo などの実処理で利用する。

## References
- [`WKEditCommand.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.h#L38)
- [`WKEditCommand.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
