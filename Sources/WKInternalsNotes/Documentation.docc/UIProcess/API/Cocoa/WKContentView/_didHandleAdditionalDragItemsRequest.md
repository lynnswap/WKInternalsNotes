# ``WKInternalsNotes/WKContentView/_didHandleAdditionalDragItemsRequest(_:)``

追加ドラッグアイテム要求の結果を処理する。

## Objective-C Declaration
```objective-c
- (void)_didHandleAdditionalDragItemsRequest:(BOOL)added;
```

## Discussion
追加要求の完了ブロックを取り出し、登録リストやステージ済みドラッグソースが無ければ空配列で完了する。条件が揃えば追加ドラッグアイテムを生成して完了し、必要に応じて `didStartDrag` を通知する。

## References
- [`WKContentViewInteraction.h#L896`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L896)
- [`WKContentViewInteraction.mm#L10627`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10627)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
