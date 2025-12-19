# ``WKInternalsNotes/WKContentView/_createTargetedContextMenuHintPreviewIfPossible()``

コンテキストメニューヒント用のターゲットプレビューを生成できる場合に返す。

## Objective-C Declaration
```objective-c
- (UITargetedPreview *)_createTargetedContextMenuHintPreviewIfPossible;
```

## Discussion
プレビュー用コンテナが表示中でない場合は `nil` を返す。リンクや画像・添付の場合は対象画像からプレビューを作り、失敗時は位置情報の矩形（必要ならデータ検出の矩形）からフォールバックプレビューを生成する。生成結果は `_contextMenuInteractionTargetedPreview` に保持される。

## References
- [`WKContentViewInteraction.h#L958`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L958)
- [`WKContentViewInteraction.mm#L11785`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11785)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
