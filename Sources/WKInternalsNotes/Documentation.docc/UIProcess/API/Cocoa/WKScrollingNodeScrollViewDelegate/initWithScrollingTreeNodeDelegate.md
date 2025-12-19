# ``WKInternalsNotes/WKScrollingNodeScrollViewDelegate/initWithScrollingTreeNodeDelegate(_:)``

Scrolling tree delegate を保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithScrollingTreeNodeDelegate:(WebKit::ScrollingTreeScrollingNodeDelegateIOS&)delegate;
```

## Discussion
`delegate` を `_scrollingTreeNodeDelegate` に保存する。

## References
- [`ScrollingTreeScrollingNodeDelegateIOS.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/ScrollingTreeScrollingNodeDelegateIOS.h#L117)
- [`ScrollingTreeScrollingNodeDelegateIOS.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/ScrollingTreeScrollingNodeDelegateIOS.mm#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
