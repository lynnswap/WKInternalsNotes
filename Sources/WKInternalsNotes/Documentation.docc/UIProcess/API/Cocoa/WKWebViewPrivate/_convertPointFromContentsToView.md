# ``WKInternalsNotes/WKWebView/_convertPointFromContentsToView(_:)``

`_convertPointFromContentsToView` を実行する。

## Objective-C Declaration
```objective-c
- (CGPoint)_convertPointFromContentsToView:(CGPoint)point WK_API_AVAILABLE(ios(10.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L729`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L729)
- [`API/ios/WKWebViewIOS.mm#L4473`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4473)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
