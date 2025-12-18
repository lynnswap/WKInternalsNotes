# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webCryptoMasterKeyForWebView(_:)``

WebCrypto のマスターキー取得を同期で要求する。

## Objective-C Declaration
```objective-c
- (NSData *)_webCryptoMasterKeyForWebView:(WKWebView *)webView;
```

## Discussion
NavigationState::NavigationClient::legacyWebCryptoMasterKey が delegate の実装を確認し、本メソッドが実装されていれば返却された NSData を Vector に変換して completionHandler に渡す。未実装の場合はデフォルトキー生成や async 版にフォールバックする。

## References
- [`WKNavigationDelegatePrivate.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L81)
- [`NavigationState.mm#L1344`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1344)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
