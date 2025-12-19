# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:runBeforeUnloadConfirmPanelWithMessage:initiatedByFrame:completionHandler:)``

beforeunload 確認パネルの結果を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView runBeforeUnloadConfirmPanelWithMessage:(NSString *)message initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(BOOL result))completionHandler WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を使い、メッセージとフレーム情報を渡して結果を受け取る。

## References
- [`WKUIDelegatePrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L158)
- [`UIDelegate.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
