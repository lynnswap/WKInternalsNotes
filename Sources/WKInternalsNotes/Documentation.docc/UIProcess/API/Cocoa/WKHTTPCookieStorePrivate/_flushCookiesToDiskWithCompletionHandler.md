# ``WKInternalsNotes/WKHTTPCookieStore/_flushCookiesToDiskWithCompletionHandler(_:)``

Cookie ストアをディスクにフラッシュする。

## Objective-C Declaration
```objective-c
- (void)_flushCookiesToDiskWithCompletionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`_protectedCookieStore->flushCookies` を呼び、完了時に completionHandler を実行する。

## References
- [`WKHTTPCookieStorePrivate.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStorePrivate.h#L31)
- [`WKHTTPCookieStore.mm#L245`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHTTPCookieStore.mm#L245)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
