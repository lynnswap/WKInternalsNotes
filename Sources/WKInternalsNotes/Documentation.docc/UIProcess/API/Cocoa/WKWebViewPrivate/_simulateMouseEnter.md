# ``WKInternalsNotes/WKWebView/_simulateMouseEnter(_:)``

`_simulateMouseEnter` を実行する。

## Objective-C Declaration
```objective-c
- (void)_simulateMouseEnter:(NSEvent *)event WK_API_AVAILABLE(macos(15.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L917`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L917)
- [`WKWebViewMac.mm#L2043`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L2043)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
