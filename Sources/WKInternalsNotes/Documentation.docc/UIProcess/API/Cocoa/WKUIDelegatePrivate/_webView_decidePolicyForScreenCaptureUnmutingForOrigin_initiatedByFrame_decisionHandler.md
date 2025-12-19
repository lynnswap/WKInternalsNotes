# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:decidePolicyForScreenCaptureUnmutingForOrigin:initiatedByFrame:decisionHandler:)``

画面キャプチャのミュート解除可否を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView decidePolicyForScreenCaptureUnmutingForOrigin:(WKSecurityOrigin *)origin initiatedByFrame:(WKFrameInfo *)frame decisionHandler:(void (^)(BOOL authorized))decisionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4));
```

## Discussion
delegate 実装時に origin と frame を渡して問い合わせ、結果を completionHandler に反映する。

## References
- [`WKUIDelegatePrivate.h#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L144)
- [`UIDelegate.mm#L1442`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1442)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
