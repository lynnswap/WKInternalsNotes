# ``WKInternalsNotes/WKTextInteractionWrapper/textInteractionAssistant``

`UIWKTextInteractionAssistant` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIWKTextInteractionAssistant *textInteractionAssistant;
```

## Default Value
`initWithView:` で生成されるが、`view.shouldUseAsyncInteractions` が `true` の場合は `nil`。

## Discussion
非同期インタラクションを使わない場合に `UIWKTextInteractionAssistant` を生成し、そのまま返す。

## References
- [`WKTextInteractionWrapper.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L72)
- [`WKTextInteractionWrapper.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L133)
- [`WKTextInteractionWrapper.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
