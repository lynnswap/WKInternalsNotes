# ``WKInternalsNotes/WKWebView/_resumePage(_:)``

`_resumePage` を実行する。

## Objective-C Declaration
```objective-c
- (void)_resumePage:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L516`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L516)
- [`API/Cocoa/WKWebView.mm#L4798`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4798)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
