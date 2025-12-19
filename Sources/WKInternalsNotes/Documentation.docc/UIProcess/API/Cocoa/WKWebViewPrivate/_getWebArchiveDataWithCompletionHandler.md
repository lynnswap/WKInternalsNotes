# ``WKInternalsNotes/WKWebView/_getWebArchiveDataWithCompletionHandler(_:)``

`_getWebArchiveDataWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getWebArchiveDataWithCompletionHandler:(void (^)(NSData *, NSError *))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L361`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L361)
- [`WKWebView.mm#L5381`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5381)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
