# ``WKInternalsNotes/WKTapHighlightView/setQuads(_:boundaryRect:)``

クワッド集合からハイライト描画領域を設定する。

## Objective-C Declaration
```objective-c
- (void)setQuads:(Vector<WebCore::FloatQuad>&&)quads boundaryRect:(const WebCore::FloatRect&)rect;
```

## Discussion
既存データをクリアし、クワッドの頂点から最小/最大範囲を算出して `viewFrame` を構築する。`viewFrame` を `4 * _minimumCornerRadius` で拡張し、`boundaryRect` と交差させた上でフレームを設定し、ローカル座標へ移動したクワッドを保持する。

## References
- [`WKTapHighlightView.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTapHighlightView.h#L41)
- [`WKTapHighlightView.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTapHighlightView.mm#L100)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
