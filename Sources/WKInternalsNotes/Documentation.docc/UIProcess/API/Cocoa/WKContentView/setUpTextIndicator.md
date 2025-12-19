# ``WKInternalsNotes/WKContentView/setUpTextIndicator(_:)``

テキストインジケータの表示を準備する。

## Objective-C Declaration
```objective-c
- (void)setUpTextIndicator:(Ref<WebCore::TextIndicator>)textIndicator;
```

## Discussion
同一インジケータなら早期リターンし、既存レイヤーを破棄したうえで `WebTextIndicatorLayer` を作成して追加する。必要に応じて `present` を実行し、フェードアウト開始を遅延スケジュールする。

## References
- [`WKContentViewInteraction.h#L928`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L928)
- [`WKContentViewInteraction.mm#L12561`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12561)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
