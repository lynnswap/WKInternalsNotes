# ``WKInternalsNotes/WKHistoryDelegatePrivate/_webView(_:didUpdateHistoryTitle:forURL:)``

履歴タイトルの更新を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didUpdateHistoryTitle:(NSString *)title forURL:(NSURL *)URL;
```

## Discussion
NavigationState::HistoryClient が delegate の応答可否を確認し、`title.createNSString()` と `NSURL` への変換結果を渡して呼び出す。delegate が未設定または未実装の場合は何も行わない。

## References
- [`WKHistoryDelegatePrivate.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHistoryDelegatePrivate.h#L40)
- [`NavigationState.mm#L1556`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1556)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
