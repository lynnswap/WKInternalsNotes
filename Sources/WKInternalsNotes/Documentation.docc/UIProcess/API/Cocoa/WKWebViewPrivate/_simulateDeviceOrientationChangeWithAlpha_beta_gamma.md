# ``WKInternalsNotes/WKWebView/_simulateDeviceOrientationChangeWithAlpha(_:beta:gamma:)``

`_simulateDeviceOrientationChangeWithAlpha` を実行する。

## Objective-C Declaration
```objective-c
- (void)_simulateDeviceOrientationChangeWithAlpha:(double)alpha beta:(double)beta gamma:(double)gamma WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L308`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L308)
- [`API/Cocoa/WKWebView.mm#L5067`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5067)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
