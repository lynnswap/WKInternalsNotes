# ``WKInternalsNotes/WKProcessPool/_cookieStoragePartitioningEnabled``

Cookie ストレージ分割の有効状態を取得・設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=_isCookieStoragePartitioningEnabled, setter=_setCookieStoragePartitioningEnabled:) BOOL _cookieStoragePartitioningEnabled WK_API_DEPRECATED("Partitioned cookies are no longer supported", macos(10.12.3, 10.14.4), ios(10.3, 12.2));
```

## Default Value
`_processPool->cookieStoragePartitioningEnabled()` の結果。

## Discussion
getter は `_processPool->cookieStoragePartitioningEnabled()` を返し、setter は `setCookieStoragePartitioningEnabled` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L181)
- [`WKProcessPool.mm#L601`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L601)
- [`WKProcessPool.mm#L606`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L606)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
