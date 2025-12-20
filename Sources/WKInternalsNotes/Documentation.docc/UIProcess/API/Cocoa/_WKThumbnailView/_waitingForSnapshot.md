# ``WKInternalsNotes/_WKThumbnailView/_waitingForSnapshot``

スナップショット取得中かどうかを示す（内部）。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign, setter=_setWaitingForSnapshot:) BOOL _waitingForSnapshot;
```

## Discussion
`requestSnapshot` で `YES` に設定し、`_didTakeSnapshot:` で `NO` に戻す。取得中の場合は `_snapshotWasDeferred` を立てて再取得を遅延する。

## References
- [`_WKThumbnailViewInternal.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailViewInternal.h#L33)
- [`_WKThumbnailView.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L133)
- [`_WKThumbnailView.mm#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L141)
- [`_WKThumbnailView.mm#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L248)
- [`_WKThumbnailView.mm#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L262)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
