# ``WKInternalsNotes/WKUIDelegatePrivate/_completeImmediateActionAnimationForWebView(_:)``

Immediate action アニメーションの完了を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_completeImmediateActionAnimationForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
`_web_completeImmediateActionAnimation` で delegate が実装済みなら呼び出し、未実装なら WebView の `_completeImmediateActionAnimation` にフォールバックする。

## References
- [`WKUIDelegatePrivate.h#L315`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L315)
- [`WKWebViewMac.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
