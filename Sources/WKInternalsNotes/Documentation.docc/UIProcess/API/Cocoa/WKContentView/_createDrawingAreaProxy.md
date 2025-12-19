# ``WKInternalsNotes/WKContentView/_createDrawingAreaProxy(_:)``

DrawingAreaProxy を生成する。

## Objective-C Declaration
```objective-c
- (Ref<WebKit::DrawingAreaProxy>)_createDrawingAreaProxy:(WebKit::WebProcessProxy&)webProcessProxy;
```

## Discussion
`RemoteLayerTreeDrawingAreaProxyIOS` を生成して返す。

## References
- [`WKContentView.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L97)
- [`WKContentView.mm#L895`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L895)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
