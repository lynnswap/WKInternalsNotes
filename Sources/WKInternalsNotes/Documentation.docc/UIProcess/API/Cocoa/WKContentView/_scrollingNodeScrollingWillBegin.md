# ``WKInternalsNotes/WKContentView/_scrollingNodeScrollingWillBegin(_:)``

スクロールノードのスクロール開始を通知する。

## Objective-C Declaration
```objective-c
- (void)_scrollingNodeScrollingWillBegin:(std::optional<WebCore::ScrollingNodeID>)nodeID;
```

## Discussion
対象ノードに対応する `UIScrollView` を取得し、`_textInteractionWrapper` にオーバーフロースクロール開始を伝える。

## References
- [`WKContentViewInteraction.h#L826`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L826)
- [`WKContentViewInteraction.mm#L2767`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2767)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
