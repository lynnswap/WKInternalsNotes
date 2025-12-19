# ``WKInternalsNotes/WKWebView/_didDisableBrowserExtensions(_:)``

`_didDisableBrowserExtensions` を実行する。

## Objective-C Declaration
```objective-c
- (void)_didDisableBrowserExtensions:(NSSet<NSString *> *)extensionIDs WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L469`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L469)
- [`WKWebView.mm#L3809`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3809)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
