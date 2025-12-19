# ``WKInternalsNotes/WKWebView/_getTextFragmentMatchWithCompletionHandler(_:)``

`_getTextFragmentMatchWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getTextFragmentMatchWithCompletionHandler:(void (^)(NSString *))completionHandler WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L371`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L371)
- [`WKWebView.mm#L5507`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5507)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
