# ``WKInternalsNotes/WKMaterialHostingView/updateHostingSize(_:)``

ホスティングビューのサイズを更新する。

## Objective-C Declaration
```objective-c
- (void)updateHostingSize:(WebCore::FloatSize)size;
```

## Discussion
`_hostingView` の frame を `(0, 0, size.width, size.height)` に設定する。

## References
- [`RemoteLayerTreeViews.h#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.h#L79)
- [`RemoteLayerTreeViews.mm#L421`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.mm#L421)
- [`RemoteLayerTreeViews.mm#L423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteLayerTreeViews.mm#L423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
