# ``WKInternalsNotes/WKWebView/_simulateMouseMove(_:)``

`_simulateMouseMove` を実行する。

## Objective-C Declaration
```objective-c
- (void)_simulateMouseMove:(NSEvent *)event WK_API_AVAILABLE(macos(13.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L916`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L916)
- [`WKWebViewMac.mm#L2038`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L2038)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
