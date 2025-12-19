# ``WKInternalsNotes/WKWebView/_updateWebpagePreferences(_:)``

`_updateWebpagePreferences` を更新する。

## Objective-C Declaration
```objective-c
- (void)_updateWebpagePreferences:(WKWebpagePreferences *)webpagePreferences WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L276`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L276)
- [`WKWebView.mm#L5233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5233)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
