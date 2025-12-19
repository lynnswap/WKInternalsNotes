# ``WKInternalsNotes/WKWebView/_setTextColor(_:sender:)``

`_setTextColor` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setTextColor:(UIColor *)color sender:(id)sender WK_API_AVAILABLE(ios(12.2));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L736`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L736)
- [`WKWebViewIOS.mm#L4514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4514)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
