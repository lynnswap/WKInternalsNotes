# ``WKInternalsNotes/WKTextInteractionWrapper/didEndScrollingOrZooming()``

スクロール/ズーム終了時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)didEndScrollingOrZooming;
```

## Discussion
`_textInteractionAssistant didEndScrollingOrZooming` を呼び、`USE(BROWSERENGINEKIT)` では保持していたフラグに応じて edit menu を再表示する。

## References
- [`WKTextInteractionWrapper.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L54)
- [`WKTextInteractionWrapper.mm#L385`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L385)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
