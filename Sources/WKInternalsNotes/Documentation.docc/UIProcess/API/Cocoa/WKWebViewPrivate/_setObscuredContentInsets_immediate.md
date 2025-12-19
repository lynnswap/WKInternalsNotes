# ``WKInternalsNotes/WKWebView/_setObscuredContentInsets(_:immediate:)``

`_setObscuredContentInsets` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setObscuredContentInsets:(NSEdgeInsets)insets immediate:(BOOL)immediate WK_API_AVAILABLE(macos(26.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L922`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L922)
- [`WKWebViewMac.mm#L1586`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1586)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
