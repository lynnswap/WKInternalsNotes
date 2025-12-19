# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:willShareActivityItems:)``

共有シート表示前にアクティビティアイテムを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willShareActivityItems:(NSArray *)activityItems WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
WKContentViewInteraction の share sheet で、表示直前に `activityItems` を通知する。

## References
- [`WKUIDelegatePrivate.h#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L176)
- [`WKContentViewInteraction.mm#L9758`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9758)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
