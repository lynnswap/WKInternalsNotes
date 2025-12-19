# ``WKInternalsNotes/WKTextInteractionWrapper/asyncTextInteraction``

BrowserEngineKit の非同期テキストインタラクションを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BETextInteraction *asyncTextInteraction;
```

## Default Value
`view.shouldUseAsyncInteractions` が `true` のとき `initWithView:` で生成され、それ以外は `nil`。

## Discussion
`USE(BROWSERENGINEKIT)` の場合に `BETextInteraction` を生成して view に追加し、保持したインスタンスを返す。

## References
- [`WKTextInteractionWrapper.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L51)
- [`WKTextInteractionWrapper.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L125)
- [`WKTextInteractionWrapper.mm#L488`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L488)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
