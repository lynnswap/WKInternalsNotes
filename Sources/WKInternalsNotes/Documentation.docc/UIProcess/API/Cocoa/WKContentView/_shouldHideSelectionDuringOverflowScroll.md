# ``WKInternalsNotes/WKContentView/_shouldHideSelectionDuringOverflowScroll(_:)``

オーバーフロースクロール中に選択を隠すか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)_shouldHideSelectionDuringOverflowScroll:(UIScrollView *)scrollView;
```

## Discussion
選択コンテナが自身の場合は常に `YES`。視覚情報が無い場合は `NO`。スクロール位置が選択コンテナと別のスクロールビューに跨る場合に `YES` を返す。

## References
- [`WKContentViewInteraction.h#L1010`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1010)
- [`WKContentViewInteraction.mm#L14283`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14283)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
