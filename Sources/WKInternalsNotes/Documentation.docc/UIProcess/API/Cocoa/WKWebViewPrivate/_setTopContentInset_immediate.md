# ``WKInternalsNotes/WKWebView/_setTopContentInset(_:immediate:)``

`_setTopContentInset` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setTopContentInset:(CGFloat)topContentInset immediate:(BOOL)immediate WK_API_AVAILABLE(macos(15.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L921`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L921)
- [`WKWebViewMac.mm#L1567`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1567)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
