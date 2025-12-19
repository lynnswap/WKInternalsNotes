# ``WKInternalsNotes/WKWebView/_clearInterfaceOrientationOverride()``

`_clearInterfaceOrientationOverride` をリセットする。

## Objective-C Declaration
```objective-c
- (void)_clearInterfaceOrientationOverride WK_API_AVAILABLE(ios(11.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L712`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L712)
- [`WKWebViewIOS.mm#L4403`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4403)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
