# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:openWindow:fromServiceWorkerOrigin:completionHandler:)``

Service Worker の openWindow 要求を処理する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore openWindow:(NSURL *)url fromServiceWorkerOrigin:(WKSecurityOrigin *)serviceWorkerOrigin completionHandler:(void (^)(WKWebView *newWebView))completionHandler;
```

## Discussion
delegate や `dataStore` が未設定の場合は `completionHandler(nil)` を呼ぶ。実装済みの場合は `CompletionHandlerCallChecker` で多重呼び出しを防ぎ、`url`/`serviceWorkerOrigin` を渡して `WKWebView` を受け取り、内部では `newWebView._page` を `WebPageProxy` に変換して利用する。

## References
- [`_WKWebsiteDataStoreDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L63)
- [`WKWebsiteDataStore.mm#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L179)
- [`WKWebsiteDataStore.mm#L197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L197)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
