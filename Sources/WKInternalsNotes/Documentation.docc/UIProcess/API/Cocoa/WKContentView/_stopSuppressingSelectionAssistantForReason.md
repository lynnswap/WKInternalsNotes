# ``WKInternalsNotes/WKContentView/_stopSuppressingSelectionAssistantForReason(_:)``

選択アシスタントの抑制を解除する。

## Objective-C Declaration
```objective-c
- (void)_stopSuppressingSelectionAssistantForReason:(WebKit::SuppressSelectionAssistantReason)reason;
```

## Discussion
指定理由を抑制理由セットから外し、抑制状態から解除されたタイミングで `[_textInteractionWrapper activateSelection]` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L766`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L766)
- [`WKContentViewInteraction.mm#L9581`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9581)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
