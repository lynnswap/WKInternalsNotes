# ``WKInternalsNotes/WKContentView/_conversationContext``

入力候補の会話コンテキストを取得・設定する。

## Objective-C Declaration
```objective-c
@property (strong, nonatomic, setter=_setConversationContext:) UIConversationContext *_conversationContext;
```

## Default Value
`_requiresLegacyTextInputTraits` に応じて legacy/extended traits の値を返す。

## Discussion
getter は legacy traits か extended traits delegate の `conversationContext` を返す。setter は両方の traits に設定し、input delegate に変更通知を行う。

## References
- [`WKContentViewInteraction.h#L1018`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1018)
- [`WKContentViewInteraction.mm#L14352`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14352)
- [`WKContentViewInteraction.mm#L14360`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14360)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
