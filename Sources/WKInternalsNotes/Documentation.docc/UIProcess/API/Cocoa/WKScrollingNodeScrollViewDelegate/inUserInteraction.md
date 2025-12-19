# ``WKInternalsNotes/WKScrollingNodeScrollViewDelegate/inUserInteraction``

ユーザー操作中かどうかを示すフラグ。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=_isInUserInteraction) BOOL inUserInteraction;
```

## Default Value
初期は `NO`。

## Discussion
`scrollViewWillBeginDragging:` で `YES` にし、`scrollViewDidEndDragging:`（減速なし）や `scrollViewDidEndDecelerating:` で `NO` に戻す。`scrollViewDidScroll:` の通知にも渡される。

## References
- [`ScrollingTreeScrollingNodeDelegateIOS.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/ScrollingTreeScrollingNodeDelegateIOS.h#L115)
- [`ScrollingTreeScrollingNodeDelegateIOS.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/ScrollingTreeScrollingNodeDelegateIOS.mm#L84)
- [`ScrollingTreeScrollingNodeDelegateIOS.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/ScrollingTreeScrollingNodeDelegateIOS.mm#L93)
- [`ScrollingTreeScrollingNodeDelegateIOS.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/ScrollingTreeScrollingNodeDelegateIOS.mm#L150)
- [`ScrollingTreeScrollingNodeDelegateIOS.mm#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/ScrollingTreeScrollingNodeDelegateIOS.mm#L163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
