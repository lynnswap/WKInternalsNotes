# ``WKInternalsNotes/WKUIDelegatePrivate/_focusWebViewFromServiceWorker(_:)``

Service Worker 由来のフォーカス要求を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (bool)_focusWebViewFromServiceWorker:(WKWebView *)webView WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
delegate 実装があれば結果を返し、未実装時は macOS でウィンドウを key/first responder にするフォールバックを行う。

## References
- [`WKUIDelegatePrivate.h#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L223)
- [`UIDelegate.mm#L894`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L894)
- [`UIDelegate.mm#L901`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L901)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
