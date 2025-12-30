# ``WKInternalsNotes/WKTapHighlightView/setFrames(_:)``

フレーム集合からハイライト描画領域を設定する。

## Objective-C Declaration
```objective-c
- (void)setFrames:(Vector<WebCore::FloatRect>&&)frames;
```

## Discussion
既存データをクリアし、空配列なら `CGRectZero` を設定する。先頭フレームは `_minimumCornerRadius` を加味して拡張し、以降は `unionRect` で `viewFrame` を構築して `setFrame:` を行う。`_innerFrames` をローカル座標へ移動して保持し、`needsDisplayOnBoundsChange` が有効なら再描画を要求する。

## References
- [`WKTapHighlightView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTapHighlightView.h#L40)
- [`WKTapHighlightView.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTapHighlightView.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
