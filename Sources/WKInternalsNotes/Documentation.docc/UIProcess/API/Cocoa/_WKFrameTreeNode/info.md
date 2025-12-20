# ``WKInternalsNotes/_WKFrameTreeNode/info``

フレームノードに対応する `WKFrameInfo` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) WKFrameInfo *info WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
内部の `FrameTreeNode` が保持する `FrameInfo` から都度生成されるため固定の既定値はない。

## Discussion
getter は `_node->info()` を `WebKit::FrameInfoData` に変換し、`API::FrameInfo::create` のラッパーを `WKFrameInfo` として返す。

## References
- [`_WKFrameTreeNode.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.h#L34)
- [`_WKFrameTreeNode.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.mm#L48)
- [`_WKFrameTreeNode.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFrameTreeNode.mm#L50)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
