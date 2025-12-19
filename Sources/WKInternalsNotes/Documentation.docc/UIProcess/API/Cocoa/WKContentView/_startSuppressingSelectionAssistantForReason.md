# ``WKInternalsNotes/WKContentView/_startSuppressingSelectionAssistantForReason(_:)``

選択アシスタントの抑制理由を追加する。

## Objective-C Declaration
```objective-c
- (void)_startSuppressingSelectionAssistantForReason:(WebKit::SuppressSelectionAssistantReason)reason;
```

## Discussion
抑制理由を記録し、初めて抑制状態になった場合は選択を非アクティブ化する。

## References
- [`WKContentViewInteraction.h#L765`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L765)
- [`WKContentViewInteraction.mm#L9572`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9572)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
