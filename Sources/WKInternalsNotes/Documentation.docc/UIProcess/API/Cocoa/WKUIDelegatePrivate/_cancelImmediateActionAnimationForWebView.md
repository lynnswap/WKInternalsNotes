# ``WKInternalsNotes/WKUIDelegatePrivate/_cancelImmediateActionAnimationForWebView(_:)``

Immediate action アニメーションのキャンセルを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_cancelImmediateActionAnimationForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
`_web_cancelImmediateActionAnimation` で delegate が実装済みなら呼び出し、未実装なら WebView の `_cancelImmediateActionAnimation` にフォールバックする。

## References
- [`WKUIDelegatePrivate.h#L313`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L313)
- [`WKWebViewMac.mm#L1307`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1307)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
