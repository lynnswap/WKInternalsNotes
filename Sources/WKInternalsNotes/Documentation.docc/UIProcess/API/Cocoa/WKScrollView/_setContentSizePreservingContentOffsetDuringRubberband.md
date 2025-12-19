# ``WKInternalsNotes/WKScrollView/_setContentSizePreservingContentOffsetDuringRubberband(_:)``

ラバーバンド中の contentSize 変更で contentOffset を保つ。

## Objective-C Declaration
```objective-c
- (void)_setContentSizePreservingContentOffsetDuringRubberband:(CGSize)contentSize;
```

## Discussion
ラバーバンド中（ドラッグ中や extents を超えた状態）に contentSize を変更する場合、現在のラバーバンド量を記録し、`setContentSize:` 後に offset を復元する。条件に当てはまらない場合はそのまま `setContentSize:` を呼ぶ。

## References
- [`WKScrollView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L40)
- [`WKScrollView.mm#L405`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L405)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
