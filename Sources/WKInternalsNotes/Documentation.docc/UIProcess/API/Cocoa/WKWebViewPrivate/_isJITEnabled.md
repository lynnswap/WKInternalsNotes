# ``WKInternalsNotes/WKWebView/_isJITEnabled(_:)``

`_isJITEnabled` の状態を返す。

## Objective-C Declaration
```objective-c
- (void)_isJITEnabled:(void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L326`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L326)
- [`API/Cocoa/WKWebView.mm#L5165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
