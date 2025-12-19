# ``WKInternalsNotes/WKWebView/_reloadWithoutContentBlockers()``

`_reloadWithoutContentBlockers` を実行する。

## Objective-C Declaration
```objective-c
- (WKNavigation *)_reloadWithoutContentBlockers WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L351`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L351)
- [`API/Cocoa/WKWebView.mm#L4919`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4919)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
