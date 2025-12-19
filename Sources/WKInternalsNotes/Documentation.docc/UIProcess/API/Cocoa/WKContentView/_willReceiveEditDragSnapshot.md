# ``WKInternalsNotes/WKContentView/_willReceiveEditDragSnapshot()``

編集ドラッグのスナップショット受信待ちを開始する。

## Objective-C Declaration
```objective-c
- (void)_willReceiveEditDragSnapshot;
```

## Discussion
`_waitingForEditDragSnapshot` を `YES` にして受信待ち状態にする。

## References
- [`WKContentViewInteraction.h#L898`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L898)
- [`WKContentViewInteraction.mm#L10810`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10810)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
