# ``WKInternalsNotes/WKViewLayoutStrategy/didChangeViewScale()``

ビューのスケール変更を通知する。

## Objective-C Declaration
```objective-c
- (void)didChangeViewScale;
```

## Discussion
基底実装は no-op。`WKViewDynamicSizeComputedFromViewScaleLayoutStrategy` は `updateLayout` を呼んで固定レイアウトサイズを再計算する。

## References
- [`WKViewLayoutStrategy.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L119)
- [`WKViewLayoutStrategy.mm#L206`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L206)
- [`WKViewLayoutStrategy.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
