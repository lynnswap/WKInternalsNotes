# ``WKInternalsNotes/WKWebView/_tryClose()``

`_tryClose` を実行する。

## Objective-C Declaration
```objective-c
- (BOOL)_tryClose WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L273`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L273)
- [`WKWebView.mm#L5012`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5012)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
