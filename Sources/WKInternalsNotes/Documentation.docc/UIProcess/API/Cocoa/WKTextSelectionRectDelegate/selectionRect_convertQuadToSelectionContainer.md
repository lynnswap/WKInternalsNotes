# ``WKInternalsNotes/WKTextSelectionRectDelegate/selectionRect(_:convertQuadToSelectionContainer:)``

クワッドを選択コンテナ座標へ変換する。

## Objective-C Declaration
```objective-c
- (WebCore::FloatQuad)selectionRect:(WKTextSelectionRect *)rect convertQuadToSelectionContainer:(const WebCore::FloatQuad&)quad;
```

## Discussion
`WKContentViewInteraction` は `_selectionContainerViewInternal` の座標空間へ `[_wk_convertQuad:toCoordinateSpace:]` で変換する。

## References
- [`WKTextSelectionRect.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextSelectionRect.h#L43)
- [`WKContentViewInteraction.mm#L6506`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6506)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
