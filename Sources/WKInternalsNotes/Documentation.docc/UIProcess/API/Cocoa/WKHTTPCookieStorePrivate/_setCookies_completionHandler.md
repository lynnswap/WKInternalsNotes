# ``WKInternalsNotes/WKHTTPCookieStore/_setCookies(_:completionHandler:)``

Cookie 配列をストアへ設定する（macOS 限定）。

## Objective-C Declaration
```objective-c
- (void)_setCookies:(NSArray<NSHTTPCookie *> *)cookies completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(26.0));
```

## Discussion
`makeVector<WebCore::Cookie>(cookies)` で変換した値を `_protectedCookieStore->setCookies` に渡し、完了時に completionHandler を実行する。`#if !TARGET_OS_IPHONE` でガードされている。

## References
- [`WKHTTPCookieStorePrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStorePrivate.h#L35)
- [`WKHTTPCookieStore.mm#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStore.mm#L254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
