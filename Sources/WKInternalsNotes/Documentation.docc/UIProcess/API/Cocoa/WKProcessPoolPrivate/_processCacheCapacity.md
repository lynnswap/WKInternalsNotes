# ``WKInternalsNotes/WKProcessPool/_processCacheCapacity()``

WebProcessCache の容量を返す。

## Objective-C Declaration
```objective-c
- (NSUInteger)_processCacheCapacity WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`_processPool->webProcessCache().capacity()` を返す。

## References
- [`WKProcessPoolPrivate.h#L147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L147)
- [`WKProcessPool.mm#L508`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L508)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
