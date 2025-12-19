# ``WKInternalsNotes/WKWebView/_setPageMuted(_:)``

`_setPageMuted` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPageMuted:(_WKMediaMutedState)mutedState WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L412`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L412)
- [`WKWebView.mm#L6111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
