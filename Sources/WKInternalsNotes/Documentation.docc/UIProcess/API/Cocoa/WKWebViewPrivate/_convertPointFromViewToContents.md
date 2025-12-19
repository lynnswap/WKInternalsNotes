# ``WKInternalsNotes/WKWebView/_convertPointFromViewToContents(_:)``

`_convertPointFromViewToContents` を実行する。

## Objective-C Declaration
```objective-c
- (CGPoint)_convertPointFromViewToContents:(CGPoint)point WK_API_AVAILABLE(ios(10.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L730`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L730)
- [`WKWebViewIOS.mm#L4478`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4478)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
