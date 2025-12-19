# ``WKInternalsNotes/WKWebView/_getContentsAsAttributedStringWithCompletionHandler(_:)``

`_getContentsAsAttributedStringWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getContentsAsAttributedStringWithCompletionHandler:(void (^)(NSAttributedString *, NSDictionary<NSAttributedStringDocumentAttributeKey, id> *, NSError *))completionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L367`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L367)
- [`WKWebView.mm#L5482`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5482)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
