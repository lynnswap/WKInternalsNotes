# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:dataInteraction:sessionWillBegin:)``

ドラッグセッション開始を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView dataInteraction:(id)interaction sessionWillBegin:(id)session WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKContentViewInteraction の `dragInteraction:sessionWillBegin:` から呼び出される。

## References
- [`WKUIDelegatePrivate.h#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L254)
- [`WKContentViewInteraction.mm#L11259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11259)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
