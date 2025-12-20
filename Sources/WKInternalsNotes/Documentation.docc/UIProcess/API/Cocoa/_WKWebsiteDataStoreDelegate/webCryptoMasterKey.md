# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/webCryptoMasterKey(_:)``

WebCrypto の master key を提供する。

## Objective-C Declaration
```objective-c
- (void)webCryptoMasterKey:(void (^)(NSData *))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0));
```

## Discussion
delegate が未設定または未実装の場合は `std::nullopt` を返す。実装済みの場合は `CompletionHandlerCallChecker` を使って一度だけ完了させ、`NSData` を byte 配列に変換して返す。`nil` が渡された場合は `std::nullopt` を返す。

## References
- [`_WKWebsiteDataStoreDelegate.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L75)
- [`WKWebsiteDataStore.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L123)
- [`WKWebsiteDataStore.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
