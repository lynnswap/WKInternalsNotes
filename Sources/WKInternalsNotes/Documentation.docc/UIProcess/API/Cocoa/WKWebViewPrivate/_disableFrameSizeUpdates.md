# ``WKInternalsNotes/WKWebView/_disableFrameSizeUpdates()``

`_disableFrameSizeUpdates` を実行する。

## Objective-C Declaration
```objective-c
- (void)_disableFrameSizeUpdates WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L885`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L885)
- [`API/mac/WKWebViewMac.mm#L1921`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1921)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
