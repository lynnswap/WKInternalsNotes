# ``WKInternalsNotes/WKEditCommand/initWithWebEditCommandProxy(_:)``

`WebEditCommandProxy` を保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithWebEditCommandProxy:(Ref<WebKit::WebEditCommandProxy>&&)command;
```

## Discussion
`WebEditCommandProxy` を `WTFMove` で `_command` に保持する。

## References
- [`WKEditCommand.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.h#L36)
- [`WKEditCommand.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.mm#L33)
- [`WKEditCommand.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKEditCommand.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
