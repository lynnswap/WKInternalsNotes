# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:dataInteraction:session:didEndWithOperation:)``

ドラッグセッション終了を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView dataInteraction:(id)interaction session:(id)session didEndWithOperation:(NSUInteger)operation WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKContentViewInteraction の `dragInteraction:session:didEndWithOperation:` から呼び出される。

## References
- [`WKUIDelegatePrivate.h#L278`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L278)
- [`WKContentViewInteraction.mm#L11274`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11274)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
