# ``WKInternalsNotes/WKModelView/initWithModel(_:layerID:page:)``

モデルデータと layerID を指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithModel:(WebCore::Model&)model layerID:(WebCore::PlatformLayerIdentifier)layerID page:(WebKit::WebPageProxy&)page NS_DESIGNATED_INITIALIZER;
```

## Discussion
`CGRectZero` で `super initWithFrame:` を呼び出した後、`_layerID` と `_page` を保持する。`createFileForModel:` でモデルを `.usdz` に書き出し、`updateBounds` を呼んでプレビュー生成を開始する。

## References
- [`WKModelView.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.h#L43)
- [`WKModelView.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.mm#L75)
- [`WKModelView.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.mm#L86)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
