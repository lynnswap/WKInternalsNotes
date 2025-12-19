# ``WKInternalsNotes/WKContentView/webSelectionRectsForSelectionGeometries(_:)``

選択ジオメトリを `WebSelectionRect` 配列に変換する。

## Objective-C Declaration
```objective-c
- (NSArray *)webSelectionRectsForSelectionGeometries:(const Vector<WebCore::SelectionGeometry>&)selectionRects;
```

## Discussion
空の場合は `nil`。各 `SelectionGeometry` の座標・方向・行情報を `WebSelectionRect` に写像して返す。

## References
- [`WKContentViewInteraction.mm#L3757`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3757)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
