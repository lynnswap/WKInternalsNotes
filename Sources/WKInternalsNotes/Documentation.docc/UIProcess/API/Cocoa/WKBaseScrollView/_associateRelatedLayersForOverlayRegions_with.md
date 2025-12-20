# ``WKInternalsNotes/WKBaseScrollView/_associateRelatedLayersForOverlayRegions(_:with:)``

オーバーレイ領域に関連するレイヤーを関連付ける。

## Objective-C Declaration
```objective-c
- (void)_associateRelatedLayersForOverlayRegions:(const HashSet<WebCore::PlatformLayerIdentifier>&)relatedLayers with:(const WebKit::RemoteLayerTreeHost&)host;
```

## Discussion
OSS の実装では no-op。内部追加実装が存在する場合はそちらが利用される。

## References
- [`WKBaseScrollView.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L69)
- [`WKBaseScrollView.mm#L265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L265)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
