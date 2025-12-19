# ``WKInternalsNotes/WKContentView/allViewsIntersectingSelectionRange``

選択範囲と交差するビューの配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<UIView *> *allViewsIntersectingSelectionRange;
```

## Default Value
選択がオーバーフロースクロールを尊重しない場合や視覚情報がない場合は空配列。

## Discussion
`selectionHonorsOverflowScrolling` が有効で視覚情報がある場合、`editorState` の `intersectingLayerIDs` から対応する `UIView` を構築して返す。

## References
- [`WKContentViewInteraction.h#L1015`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1015)
- [`WKContentViewInteraction.mm#L14270`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14270)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
