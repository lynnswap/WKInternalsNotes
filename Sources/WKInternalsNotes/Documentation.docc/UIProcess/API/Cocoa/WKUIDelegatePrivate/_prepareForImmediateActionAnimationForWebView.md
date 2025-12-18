# ``WKInternalsNotes/WKUIDelegatePrivate/_prepareForImmediateActionAnimationForWebView(_:)``

Immediate action アニメーション開始前の準備を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_prepareForImmediateActionAnimationForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
`_web_prepareForImmediateActionAnimation` で delegate が実装済みなら呼び出し、未実装なら WebView の `_prepareForImmediateActionAnimation` にフォールバックする。

## References
- [`WKUIDelegatePrivate.h#L312`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L312)
- [`WKWebViewMac.mm#L1298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1298)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
