# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webCryptoMasterKeyForWebView(_:completionHandler:)``

WebCrypto のマスターキー取得を非同期で要求する。

## Objective-C Declaration
```objective-c
- (void)_webCryptoMasterKeyForWebView:(WKWebView *)webView completionHandler:(void (^)(NSData *))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
legacyWebCryptoMasterKey が sync 版未実装かつ本メソッド実装時に、CompletionHandlerCallChecker 付きで呼び出し、NSData を Vector に変換して completionHandler に渡す。nil の場合は std::nullopt。

## References
- [`WKNavigationDelegatePrivate.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L81)
- [`NavigationState.mm#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L222)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
