# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestStorageAccessPanelForDomain:underCurrentDomain:forQuirkDomains:completionHandler:)``

quirk ドメイン情報付きでストレージアクセスパネルを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestStorageAccessPanelForDomain:(NSString *)requestingDomain underCurrentDomain:(NSString *)currentDomain forQuirkDomains:(NSDictionary<NSString *, NSArray<NSString *> *> *)quirkDomains completionHandler:(void (^)(BOOL result))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
拡張 API が実装されている場合に quirk ドメイン辞書を渡して判断を求める。

## References
- [`WKUIDelegatePrivate.h#L188`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L188)
- [`UIDelegate.mm#L538`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L538)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
