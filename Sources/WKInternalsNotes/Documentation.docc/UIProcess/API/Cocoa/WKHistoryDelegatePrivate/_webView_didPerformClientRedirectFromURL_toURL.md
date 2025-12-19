# ``WKInternalsNotes/WKHistoryDelegatePrivate/_webView(_:didPerformClientRedirectFromURL:toURL:)``

クライアントリダイレクトを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didPerformClientRedirectFromURL:(NSURL *)sourceURL toURL:(NSURL *)destinationURL;
```

## Discussion
NavigationState::HistoryClient が delegate の応答可否を確認し、`[NSURL _web_URLWithWTFString:]` で変換した URL を渡して呼び出す。delegate が未設定または未実装の場合は何も行わない。

## References
- [`WKHistoryDelegatePrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHistoryDelegatePrivate.h#L37)
- [`NavigationState.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
