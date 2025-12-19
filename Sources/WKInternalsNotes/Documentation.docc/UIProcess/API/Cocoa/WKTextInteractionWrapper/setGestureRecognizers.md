# ``WKInternalsNotes/WKTextInteractionWrapper/setGestureRecognizers()``

テキスト操作のジェスチャ認識を設定する。

## Objective-C Declaration
```objective-c
- (void)setGestureRecognizers;
```

## Discussion
`_textInteractionAssistant setGestureRecognizers` を呼び出し、`USE(BROWSERENGINEKIT)` では `editabilityChanged` も通知する。

## References
- [`WKTextInteractionWrapper.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L44)
- [`WKTextInteractionWrapper.mm#L324`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L324)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
