# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:showCustomSheetForElement:)``

要素に対するカスタムシート表示を delegate に委ねる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView showCustomSheetForElement:(_WKActivatedElementInfo *)element WK_API_DEPRECATED_WITH_REPLACEMENT("_webView:contextMenuConfigurationForElement:completionHandler:", ios(10.0, 13.0));
```

## Discussion
WKContentViewInteraction の `_showAttachmentSheet` で、`_WKActivatedElementInfo` を渡して旧 API として呼び出される。

## References
- [`WKUIDelegatePrivate.h#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L237)
- [`WKContentViewInteraction.mm#L3217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3217)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
