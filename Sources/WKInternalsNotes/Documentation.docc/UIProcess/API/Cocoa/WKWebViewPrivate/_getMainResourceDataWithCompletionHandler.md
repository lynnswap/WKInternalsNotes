# ``WKInternalsNotes/WKWebView/_getMainResourceDataWithCompletionHandler(_:)``

`_getMainResourceDataWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getMainResourceDataWithCompletionHandler:(void (^)(NSData *, NSError *))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L360`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L360)
- [`WKWebView.mm#L5373`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5373)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
