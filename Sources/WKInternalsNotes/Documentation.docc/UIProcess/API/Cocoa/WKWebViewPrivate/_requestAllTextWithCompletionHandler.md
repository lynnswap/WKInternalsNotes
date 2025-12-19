# ``WKInternalsNotes/WKWebView/_requestAllTextWithCompletionHandler(_:)``

`_requestAllTextWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestAllTextWithCompletionHandler:(void(^)(NSArray<_WKTextRun *> *))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L611`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L611)
- [`WKWebView.mm#L4551`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4551)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
