# ``WKInternalsNotes/_WKThumbnailView/_sublayerTranslation``

サブレイヤーの平行移動量を設定する（内部）。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign, setter=_setSublayerTranslation:) CGPoint _sublayerTranslation;
```

## Discussion
`_setSublayerTranslation:` は差分分だけ `sublayerTransform` を更新し、値を保持する。`_viewWasParented` では obscured content insets に合わせた負のオフセットを設定する。

## References
- [`_WKThumbnailViewInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailViewInternal.h#L34)
- [`_WKThumbnailView.mm#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L222)
- [`_WKThumbnailView.mm#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L292)
- [`_WKThumbnailView.mm#L297`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L297)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
