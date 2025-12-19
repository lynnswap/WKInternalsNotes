# ``WKInternalsNotes/WKWebView/_propertiesOfLayerWithID(_:)``

`_propertiesOfLayerWithID` を実行する。

## Objective-C Declaration
```objective-c
- (NSDictionary<NSString *, id> *)_propertiesOfLayerWithID:(unsigned long long)layerID;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L57)
- [`WKWebViewTesting.mm#L974`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L974)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
