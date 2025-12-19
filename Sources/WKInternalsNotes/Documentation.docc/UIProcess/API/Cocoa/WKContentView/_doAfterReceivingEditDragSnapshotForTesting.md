# ``WKInternalsNotes/WKContentView/_doAfterReceivingEditDragSnapshotForTesting(_:)``

編集ドラッグのスナップショット取得後にアクションを実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterReceivingEditDragSnapshotForTesting:(dispatch_block_t)action;
```

## Discussion
`ENABLE(DRAG_SUPPORT)` かつスナップショット待ちの場合はアクションを保持し、そうでなければ即時実行する。

## References
- [`WKContentViewInteraction.h#L1040`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1040)
- [`WKContentViewInteraction.mm#L14415`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14415)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
