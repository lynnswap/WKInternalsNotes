# ``WKInternalsNotes/WKContentView/textInteractionAssistant``

テキスト操作支援用の `UIWKTextInteractionAssistant` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIWKTextInteractionAssistant *textInteractionAssistant;
```

## Default Value
`_textInteractionWrapper` が保持する `textInteractionAssistant` を返す。

## Discussion
`_textInteractionWrapper` から `textInteractionAssistant` を取得して返す。

## References
- [`WKContentViewInteraction.h#L1073`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1073)
- [`WKContentViewInteraction.mm#L14707`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14707)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
