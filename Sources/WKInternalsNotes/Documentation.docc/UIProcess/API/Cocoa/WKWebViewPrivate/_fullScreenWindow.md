# ``WKInternalsNotes/WKWebView/_fullScreenWindow()``

`_fullScreenWindow` を実行する。

## Objective-C Declaration
```objective-c
- (NSWindow *)_fullScreenWindow WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L898`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L898)
- [`WKWebViewMac.mm#L1973`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1973)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
