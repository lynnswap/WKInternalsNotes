# ``WKInternalsNotes/WKWebView/_setFontSize(_:sender:)``

`_setFontSize` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setFontSize:(CGFloat)fontSize sender:(id)sender WK_API_AVAILABLE(ios(12.2));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L735`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L735)
- [`WKWebViewIOS.mm#L4508`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4508)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
