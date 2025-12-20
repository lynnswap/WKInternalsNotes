# ``WKInternalsNotes/_WKThumbnailView/maximumSnapshotSize``

スナップショットの最大サイズ制約を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGSize maximumSnapshotSize;
```

## Default Value
`CGSizeZero` の場合は制約なし。

## Discussion
`requestSnapshot` で `bitmapSize` を最大サイズに合わせてスケールし、`setMaximumSnapshotSize:` で値が変わると再スナップショットを要求する。

## References
- [`_WKThumbnailView.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L46)
- [`_WKThumbnailView.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L154)
- [`_WKThumbnailView.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L156)
- [`_WKThumbnailView.mm#L301`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L301)
- [`_WKThumbnailView.mm#L306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L306)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
