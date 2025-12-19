# ``WKInternalsNotes/WKTextInteractionWrapper/prepareToMoveSelectionContainer(_:)``

選択表示のコンテナ移動に備えてビュー配置を調整する。

## Objective-C Declaration
```objective-c
- (void)prepareToMoveSelectionContainer:(UIView *)newContainer;
```

## Discussion
`highlightView` が `newContainer` に存在しない場合は display interaction を再接続し、追加された選択関連ビューを `_managedTextSelectionViews` として記録する。`newContainer` が `_view` 以外の場合は、タイルグリッドや選択範囲に重なるビューの順序を考慮して managed selection views を挿入し直す。

## References
- [`WKTextInteractionWrapper.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L58)
- [`WKTextInteractionWrapper.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
