# ``WKInternalsNotes/_WKTargetedElementInfo/takeSnapshotWithCompletionHandler(_:)``

要素のスナップショットを非同期に取得する。

## Objective-C Declaration
```objective-c
- (void)takeSnapshotWithCompletionHandler:(void(^)(CGImageRef))completionHandler;
```

## Discussion
`_info->takeSnapshot` で `ShareableBitmapHandle` を受け取り、存在すれば `ShareableBitmap` 経由で `CGImageRef` を生成して渡す。生成できない場合は `nullptr` を返す。

## References
- [`_WKTargetedElementInfo.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L67)
- [`_WKTargetedElementInfo.mm#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L192)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
