# ``WKInternalsNotes/WKContentView/containerForContextMenuHintPreviews()``

コンテキストメニューヒント用プレビューのコンテナを返す。

## Objective-C Declaration
```objective-c
- (UIView *)containerForContextMenuHintPreviews;
```

## Discussion
未生成なら専用コンテナを作成し、`WKUIDelegatePrivate` が提供するコンテナがあればそこに、無ければ `_interactionViewsContainerView` に追加する。

## References
- [`WKContentViewInteraction.h#L954`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L954)
- [`WKContentViewInteraction.mm#L10319`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10319)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
