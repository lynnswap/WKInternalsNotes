# ``WKInternalsNotes/WKWebView/_snapshotLayerContentsForBackForwardListItem(_:)``

`_snapshotLayerContentsForBackForwardListItem` を実行する。

## Objective-C Declaration
```objective-c
- (id)_snapshotLayerContentsForBackForwardListItem:(WKBackForwardListItem *)item WK_API_AVAILABLE(ios(9_0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L773`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L773)
- [`API/ios/WKWebViewIOS.mm#L4987`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4987)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
