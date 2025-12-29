# ``WKInternalsNotes/WKInspectorHighlightView/update(_:scale:frame:)``

ハイライトの内容・スケール・フレームを更新し、表示レイヤーを再構成する。

## Objective-C Declaration
```objective-c
- (void)update:(const WebCore::InspectorOverlay::Highlight&)highlight scale:(double)scale frame:(const WebCore::FloatRect&)frame;
```

## Discussion
全レイヤーを削除して `_highlight` を更新し、`contentScaleFactor` を `UIScreen.mainScreen.scale * scale` に設定して `frame` を更新する。`highlight.type` が `Node`/`NodeList` の場合は `_layoutForNodeListHighlight:`、`Rects` の場合は `_layoutForRectsHighlight:` を実行し、最後に `setNeedsDisplay` で再描画を要求する。

## References
- [`WKInspectorHighlightView.mm#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/ios/WKInspectorHighlightView.mm#L286)
- [`WKInspectorHighlightView.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/ios/WKInspectorHighlightView.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
