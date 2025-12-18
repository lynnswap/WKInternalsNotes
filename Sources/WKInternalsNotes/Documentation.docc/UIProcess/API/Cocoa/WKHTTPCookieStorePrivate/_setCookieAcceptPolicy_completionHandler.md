# ``WKInternalsNotes/WKHTTPCookieStore/_setCookieAcceptPolicy(_:completionHandler:)``

Cookie 受け入れポリシーを設定する。

## Objective-C Declaration
```objective-c
- (void)_setCookieAcceptPolicy:(NSHTTPCookieAcceptPolicy)policy completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`WebCore::toHTTPCookieAcceptPolicy(policy)` で変換した値を `setHTTPCookieAcceptPolicy` に渡し、完了後に completionHandler を呼ぶ。

## References
- [`WKHTTPCookieStorePrivate.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStorePrivate.h#L30)
- [`WKHTTPCookieStore.mm#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStore.mm#L238)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
