# ``WKInternalsNotes/WKWebView/_visitUnsafeWebsiteSentinel()``

`_visitUnsafeWebsiteSentinel` を実行する。

## Objective-C Declaration
```objective-c
+ (NSURL *)_visitUnsafeWebsiteSentinel WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L314`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L314)
- [`API/Cocoa/WKWebView.mm#L5160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
