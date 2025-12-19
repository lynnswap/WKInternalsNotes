# ``WKInternalsNotes/WKWebView/_setFrame(_:andScrollBy:)``

`_setFrame` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setFrame:(NSRect)rect andScrollBy:(NSSize)offset WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L881`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L881)
- [`WKWebViewMac.mm#L1906`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1906)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
