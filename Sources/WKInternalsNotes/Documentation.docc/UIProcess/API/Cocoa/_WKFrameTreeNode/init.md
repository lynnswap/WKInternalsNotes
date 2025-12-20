# ``WKInternalsNotes/_WKFrameTreeNode/init()``

直接初期化できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
ヘッダで `NS_UNAVAILABLE` 指定のため `init` は使用できない。インスタンスは `API::FrameTreeNode::create` で生成され、`wrapper(...)` 経由で `_WKFrameTreeNode` として渡される。

## References
- [`_WKFrameTreeNode.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.h#L32)
- [`_WKFrameTreeNodeInternal.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNodeInternal.h#L33)
- [`_WKFrameTreeNode.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
