# ``WKInternalsNotes/WKProcessPool/_allProcessPoolsForTesting()``

全てのプロセスプールを配列で返す（テスト用）。

## Objective-C Declaration
```objective-c
+ (NSArray<WKProcessPool *> *)_allProcessPoolsForTesting WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`WebKit::WebProcessPool::allProcessPools()` の各要素を `wrapper(...)` で包み、`NSArray` として返す。

## References
- [`WKProcessPoolPrivate.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L82)
- [`WKProcessPool.mm#L206`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L206)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
