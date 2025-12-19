# ``WKInternalsNotes/WKWebView/_layerForFindOverlay``

`_layerForFindOverlay` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CALayer *_layerForFindOverlay WK_API_AVAILABLE(ios(16.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L679`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L679)
- [`WKWebViewIOS.mm#L3849`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L3849)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
