# ``WKInternalsNotes/_WKFrameTreeNode/childFrames``

子フレームに対応する `_WKFrameTreeNode` 配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<_WKFrameTreeNode *> *childFrames;
```

## Default Value
子フレームが存在しない場合は空配列になる。

## Discussion
内部の `FrameTreeNode` が持つ `childFrames()` を列挙し、各要素を `WebKit::FrameTreeNodeData` 経由で `API::FrameTreeNode::create` に渡してラップする。

## References
- [`_WKFrameTreeNode.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.h#L35)
- [`_WKFrameTreeNode.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.mm#L53)
- [`_WKFrameTreeNode.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.mm#L55)
- [`_WKFrameTreeNode.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
