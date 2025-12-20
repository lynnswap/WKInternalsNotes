# ``WKInternalsNotes/_WKThumbnailView/requestSnapshot()``

スナップショット取得を要求する。

## Objective-C Declaration
```objective-c
- (void)requestSnapshot;
```

## Discussion
取得中の場合は `_snapshotWasDeferred` を立てて終了する。`WebPageProxy` から viewSize と obscuredContentInsets を取得して `snapshotRect` を計算し、`_scale` と device scale factor を反映した `bitmapSize` を生成する。`maximumSnapshotSize` が設定されている場合はサイズ制約を適用し、`takeSnapshot` を呼び出す。

## References
- [`_WKThumbnailView.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L54)
- [`_WKThumbnailView.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L133)
- [`_WKThumbnailView.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L135)
- [`_WKThumbnailView.mm#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L143)
- [`_WKThumbnailView.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L150)
- [`_WKThumbnailView.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L154)
- [`_WKThumbnailView.mm#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
