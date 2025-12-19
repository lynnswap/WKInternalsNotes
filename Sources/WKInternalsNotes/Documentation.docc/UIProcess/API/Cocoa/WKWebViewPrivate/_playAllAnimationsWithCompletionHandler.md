# ``WKInternalsNotes/WKWebView/_playAllAnimationsWithCompletionHandler(_:)``

`_playAllAnimationsWithCompletionHandler` を実行する。

## Objective-C Declaration
```objective-c
- (void)_playAllAnimationsWithCompletionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L605`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L605)
- [`WKWebView.mm#L4403`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4403)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
