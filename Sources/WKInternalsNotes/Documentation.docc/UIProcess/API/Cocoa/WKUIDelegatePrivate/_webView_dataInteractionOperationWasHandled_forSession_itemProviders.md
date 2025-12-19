# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:dataInteractionOperationWasHandled:forSession:itemProviders:)``

ドラッグ/ドロップ操作の処理結果を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView dataInteractionOperationWasHandled:(BOOL)handled forSession:(id)session itemProviders:(NSArray *)itemProviders WK_API_AVAILABLE(ios(11.0));
```

## Discussion
ドロップ処理完了後に `handled` と `itemProviders` を渡して delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L256`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L256)
- [`WKContentViewInteraction.mm#L10861`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10861)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
