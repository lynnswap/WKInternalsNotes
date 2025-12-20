# ``WKInternalsNotes/_WKThumbnailView/_thumbnailLayer``

サムネイル用レイヤーを取得・設定する（内部）。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign, setter=_setThumbnailLayer:) CALayer *_thumbnailLayer;
```

## Discussion
`_setThumbnailLayer:` は `layer.sublayers` に渡されたレイヤーを 1 件だけ設定する。getter は `sublayers` の先頭を返し、存在しない場合は `nil` を返す。

## References
- [`_WKThumbnailViewInternal.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailViewInternal.h#L32)
- [`_WKThumbnailView.mm#L311`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L311)
- [`_WKThumbnailView.mm#L316`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L316)
- [`_WKThumbnailView.mm#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L321)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
