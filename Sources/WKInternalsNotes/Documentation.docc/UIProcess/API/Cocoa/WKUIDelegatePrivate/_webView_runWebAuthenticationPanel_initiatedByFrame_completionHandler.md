# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:runWebAuthenticationPanel:initiatedByFrame:completionHandler:)``

Web Authentication パネルの表示を delegate に依頼する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView runWebAuthenticationPanel:(_WKWebAuthenticationPanel *)panel initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(_WKWebAuthenticationPanelResult))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を使い、パネルと `WKFrameInfo` を渡して結果を受け取る。

## References
- [`WKUIDelegatePrivate.h#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L172)
- [`UIDelegate.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
