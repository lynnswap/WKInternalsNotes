# ``WKInternalsNotes/WKWebView/_isClosed()``

`_isClosed` の状態を返す。

## Objective-C Declaration
```objective-c
- (BOOL)_isClosed WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L274`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L274)
- [`API/Cocoa/WKWebView.mm#L5018`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5018)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
