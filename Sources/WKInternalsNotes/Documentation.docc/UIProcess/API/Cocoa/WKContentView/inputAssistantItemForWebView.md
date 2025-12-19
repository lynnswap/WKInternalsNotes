# ``WKInternalsNotes/WKContentView/inputAssistantItemForWebView``

WebView 向けの `UITextInputAssistantItem` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UITextInputAssistantItem *inputAssistantItemForWebView;
```

## Default Value
`super` の `inputAssistantItem` を返す。

## Discussion
`WKContentView` 自体の `inputAssistantItem` ではなく、`super` 実装の `inputAssistantItem` を返す。

## References
- [`WKContentViewInteraction.h#L728`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L728)
- [`WKContentViewInteraction.mm#L4250`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4250)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
