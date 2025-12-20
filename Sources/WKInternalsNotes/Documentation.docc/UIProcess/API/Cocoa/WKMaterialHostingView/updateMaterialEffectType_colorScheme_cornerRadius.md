# ``WKInternalsNotes/WKMaterialHostingView/updateMaterialEffectType(_:colorScheme:cornerRadius:)``

マテリアル効果の種類・配色・角丸を更新する。

## Objective-C Declaration
```objective-c
- (void)updateMaterialEffectType:(WKHostedMaterialEffectType)materialEffectType colorScheme:(WKHostedMaterialColorScheme)colorScheme cornerRadius:(CGFloat)cornerRadius;
```

## Discussion
`WKMaterialHostingSupport` に `_hostingView` と `_contentView` を渡して更新を委譲する。

## References
- [`RemoteLayerTreeViews.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.h#L80)
- [`RemoteLayerTreeViews.mm#L426`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.mm#L426)
- [`RemoteLayerTreeViews.mm#L428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.mm#L428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
