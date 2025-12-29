# ``WKInternalsNotes/WKViewLayoutStrategy/didChangeFrameSize()``

ビューのフレームサイズ変更を通知する。

## Objective-C Declaration
```objective-c
- (void)didChangeFrameSize;
```

## Discussion
基底実装は `clipsToVisibleRect` の場合に露出領域を更新し、`WebViewImpl` の描画領域サイズをビューのフレームに合わせて更新する。`WKViewDynamicSizeComputedFromViewScaleLayoutStrategy` は `frameSizeUpdatesDisabled` が `NO` の場合に追加で `updateLayout` を実行する。

## References
- [`WKViewLayoutStrategy.mm#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L131)
- [`WKViewLayoutStrategy.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L213)
- [`WKViewLayoutStrategy.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
