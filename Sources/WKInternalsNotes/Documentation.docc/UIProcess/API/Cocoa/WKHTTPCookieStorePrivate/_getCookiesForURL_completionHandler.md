# ``WKInternalsNotes/WKHTTPCookieStore/_getCookiesForURL(_:completionHandler:)``

指定 URL に対する Cookie を取得して返す。

## Objective-C Declaration
```objective-c
- (void)_getCookiesForURL:(NSURL *)url completionHandler:(void (^)(NSArray<NSHTTPCookie *> *))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`_protectedCookieStore->isOptInCookiePartitioningEnabled()` を取得した上で `cookiesForURL` を呼び、`coreCookiesToNSCookies` で変換した配列を completionHandler に渡す。

## References
- [`WKHTTPCookieStorePrivate.h#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStorePrivate.h#L29)
- [`WKHTTPCookieStore.mm#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStore.mm#L230)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
