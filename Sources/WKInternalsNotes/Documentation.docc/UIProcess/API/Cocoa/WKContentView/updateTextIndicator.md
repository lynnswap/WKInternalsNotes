# ``WKInternalsNotes/WKContentView/updateTextIndicator(_:)``

テキストインジケータの表示を更新する。

## Objective-C Declaration
```objective-c
- (void)updateTextIndicator:(Ref<WebCore::TextIndicator>)textIndicator;
```

## Discussion
現在の `_textIndicator` と一致する場合のみ、新しい `WebTextIndicatorLayer` を作成してレイヤーに追加する。

## References
- [`WKContentViewInteraction.h#L929`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L929)
- [`WKContentViewInteraction.mm#L12583`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12583)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
