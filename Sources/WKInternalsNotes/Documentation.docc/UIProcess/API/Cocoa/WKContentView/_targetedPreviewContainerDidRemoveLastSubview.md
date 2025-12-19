# ``WKInternalsNotes/WKContentView/_targetedPreviewContainerDidRemoveLastSubview(_:)``

ターゲットプレビュー用コンテナの最終サブビュー削除を処理する。

## Objective-C Declaration
```objective-c
- (void)_targetedPreviewContainerDidRemoveLastSubview:(WKTargetedPreviewContainer *)containerView;
```

## Discussion
対象コンテナが `_contextMenuHintContainerView` と一致する場合に `_removeContextMenuHintContainerIfPossible` を呼び、必要ならコンテナを片付ける。

## References
- [`WKContentViewInteraction.h#L960`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L960)
- [`WKContentViewInteraction.mm#L10197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10197)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
