# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestStorageAccessPanelForDomain:underCurrentDomain:completionHandler:)``

ストレージアクセスパネルの表示可否を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestStorageAccessPanelForDomain:(NSString *)requestingDomain underCurrentDomain:(NSString *)currentDomain completionHandler:(void (^)(BOOL result))completionHandler WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を用いて要求元/現在ドメインを渡し、結果を completionHandler に返す。

## References
- [`WKUIDelegatePrivate.h#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L163)
- [`UIDelegate.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
