# ``WKInternalsNotes/WKProcessPool/_getActivePagesOriginsInWebProcessForTesting(_:completionHandler:)``

指定 WebProcess のアクティブページ origin を取得する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_getActivePagesOriginsInWebProcessForTesting:(pid_t)pid completionHandler:(void(^)(NSArray<NSString *> *))completionHandler WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`activePagesOriginsInWebProcessForTesting` の `Vector<String>` を `NSArray` に変換して completionHandler に渡す。

## References
- [`WKProcessPoolPrivate.h#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L179)
- [`WKProcessPool.mm#L626`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L626)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
