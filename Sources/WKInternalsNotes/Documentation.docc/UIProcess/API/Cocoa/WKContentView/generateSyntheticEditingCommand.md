# ``WKInternalsNotes/WKContentView/generateSyntheticEditingCommand(_:)``

編集コマンドを合成して実行する。

## Objective-C Declaration
```objective-c
- (void)generateSyntheticEditingCommand:(WebKit::SyntheticEditingCommandType)command;
```

## Discussion
`WebPageProxy::generateSyntheticEditingCommand` に委譲する。

## References
- [`WKContentViewInteraction.h#L863`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L863)
- [`WKContentViewInteraction.mm#L7626`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7626)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
