# ``WKInternalsNotes/WKExtendedTextInputTraits/conversationContext``

会話コンテキストを保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) UIConversationContext *conversationContext;
```

## Default Value
初期値は `nil`。

## Discussion
`HAVE(UI_CONVERSATION_CONTEXT)` の場合に `_conversationContext` を保持して返す。

## References
- [`WKExtendedTextInputTraits.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L63)
- [`WKExtendedTextInputTraits.mm#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L107)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
