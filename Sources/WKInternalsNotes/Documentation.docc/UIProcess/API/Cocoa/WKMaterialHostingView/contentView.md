# ``WKInternalsNotes/WKMaterialHostingView/contentView``

ホスティング対象の contentView を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *contentView;
```

## Default Value
`init` で生成した `UIView`。

## Discussion
`init` で `UIView` を生成して `_contentView` に保持し、このプロパティで返す。`HAVE(MATERIAL_HOSTING)` の場合のみ有効。

## References
- [`RemoteLayerTreeViews.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.h#L77)
- [`RemoteLayerTreeViews.mm#L408`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.mm#L408)
- [`RemoteLayerTreeViews.mm#L416`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.mm#L416)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
