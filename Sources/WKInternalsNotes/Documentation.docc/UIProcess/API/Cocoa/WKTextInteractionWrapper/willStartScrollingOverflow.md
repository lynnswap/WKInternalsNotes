# ``WKInternalsNotes/WKTextInteractionWrapper/willStartScrollingOverflow(_:)``

オーバーフロースクロール開始に合わせて edit menu を抑制する。

## Objective-C Declaration
```objective-c
- (void)willStartScrollingOverflow:(UIScrollView *)scrollView;
```

## Discussion
既存の `HideEditMenuScope` があれば何もしない。`_view _shouldHideSelectionDuringOverflowScroll:` の結果で選択を非アクティブ化するか決め、`HideEditMenuScope` を作成する。

## References
- [`WKTextInteractionWrapper.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L45)
- [`WKTextInteractionWrapper.mm#L355`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L355)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
