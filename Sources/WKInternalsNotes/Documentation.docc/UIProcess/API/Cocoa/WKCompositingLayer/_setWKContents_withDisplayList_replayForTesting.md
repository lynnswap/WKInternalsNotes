# ``WKInternalsNotes/WKCompositingLayer/_setWKContents(_:withDisplayList:replayForTesting:)``

動的コンテンツスケーリング用の表示内容を設定する。

## Objective-C Declaration
```objective-c
- (void)_setWKContents:(id)contents withDisplayList:(WebCore::DynamicContentScalingDisplayList&&)data replayForTesting:(BOOL)replay;
```

## Discussion
`displayList` から `CFData` を生成し、`replay` が `YES` の場合はテスト用に保持して `setNeedsDisplay` する。通常時は `contents` を設定し、`displayList` から取り出したサーフェスを `CAMachPort` に変換して `WKDynamicContentScalingContentsKey`/`WKDynamicContentScalingPortsKey` にセットした上で再描画する。

## References
- [`RemoteLayerTreeLayers.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/cocoa/RemoteLayerTreeLayers.h#L40)
- [`RemoteLayerTreeLayers.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/cocoa/RemoteLayerTreeLayers.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
