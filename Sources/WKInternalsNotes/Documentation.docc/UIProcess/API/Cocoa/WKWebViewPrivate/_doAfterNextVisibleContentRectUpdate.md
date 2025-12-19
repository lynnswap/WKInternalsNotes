# ``WKInternalsNotes/WKWebView/_doAfterNextVisibleContentRectUpdate(_:)``

`_doAfterNextVisibleContentRectUpdate` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterNextVisibleContentRectUpdate:(void (^)(void))updateBlock WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L322`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L322)
- [`API/Cocoa/WKWebView.mm#L6157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6157)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
