# ``WKInternalsNotes/WKWebView/_getProcessDisplayNameWithCompletionHandler(_:)``

`_getProcessDisplayNameWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getProcessDisplayNameWithCompletionHandler:(void (^)(NSString *))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L459`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L459)
- [`API/Cocoa/WKWebView.mm#L5993`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5993)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
