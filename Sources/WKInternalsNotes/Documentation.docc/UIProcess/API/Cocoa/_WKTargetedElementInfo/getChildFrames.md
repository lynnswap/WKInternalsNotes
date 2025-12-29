# ``WKInternalsNotes/_WKTargetedElementInfo/getChildFrames(_:)``

子フレームの情報を非同期に取得する。

## Objective-C Declaration
```objective-c
- (void)getChildFrames:(void(^)(NSArray<_WKFrameTreeNode *> *))completionHandler;
```

## Discussion
`_info->childFrames` の結果を `_WKFrameTreeNode` に変換して `completionHandler` に渡す。

## References
- [`_WKTargetedElementInfo.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L66)
- [`_WKTargetedElementInfo.mm#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L138)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
