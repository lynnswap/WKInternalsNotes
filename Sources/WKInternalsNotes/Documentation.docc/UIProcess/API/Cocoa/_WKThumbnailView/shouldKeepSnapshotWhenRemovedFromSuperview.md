# ``WKInternalsNotes/_WKThumbnailView/shouldKeepSnapshotWhenRemovedFromSuperview``

ビューが外れたときにスナップショットを保持するかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldKeepSnapshotWhenRemovedFromSuperview;
```

## Default Value
`NO`。

## Discussion
`NO` の場合は `_viewWasUnparented` で `layer.contents` をクリアし、スナップショットを破棄する。`YES` の場合はそのまま保持する。

## References
- [`_WKThumbnailView.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L50)
- [`_WKThumbnailView.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L202)
- [`_WKThumbnailView.mm#L205`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L205)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
