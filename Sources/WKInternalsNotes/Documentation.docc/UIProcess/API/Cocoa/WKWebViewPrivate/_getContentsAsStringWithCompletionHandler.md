# ``WKInternalsNotes/WKWebView/_getContentsAsStringWithCompletionHandler(_:)``

`_getContentsAsStringWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getContentsAsStringWithCompletionHandler:(void (^)(NSString *, NSError *))completionHandler WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L364`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L364)
- [`WKWebView.mm#L5458`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5458)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
