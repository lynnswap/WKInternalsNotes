# ``WKInternalsNotes/_WKIconLoadingDelegate/webView(_:shouldLoadIconWithParameters:completionHandler:)``

アイコン読み込みの可否と取得方法を delegate に委ねる。

## Objective-C Declaration
```objective-c
- (void)webView:(WKWebView *)webView shouldLoadIconWithParameters:(_WKLinkIconParameters *)parameters completionHandler:(void (^)(void (^)(NSData*)))completionHandler;
```

## Discussion
HTTP/HTTPS または `data:` の URL のみ対象で、delegate 未設定/未実装の場合は `completionHandler(nil)` を返す。`_WKLinkIconParameters` を生成して delegate を呼び出し、delegate が渡した `loadCompletionHandler` があれば `API::Data*` を `NSData` に変換して実行する。

## References
- [`_WKIconLoadingDelegate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKIconLoadingDelegate.h#L35)
- [`IconLoadingDelegate.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/IconLoadingDelegate.mm#L80)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
