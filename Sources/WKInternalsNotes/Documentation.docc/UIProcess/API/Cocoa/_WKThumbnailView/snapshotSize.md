# ``WKInternalsNotes/_WKThumbnailView/snapshotSize``

最新のスナップショットサイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize snapshotSize;
```

## Default Value
スナップショット取得後に `CGImage` のサイズで更新される。

## Discussion
`_didTakeSnapshot:` で `snapshotSize` を更新し、KVO 通知を行う。

## References
- [`_WKThumbnailView.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L45)
- [`_WKThumbnailView.mm#L243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L243)
- [`_WKThumbnailView.mm#L247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L247)
- [`_WKThumbnailView.mm#L268`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L268)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
