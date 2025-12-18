# ``WKInternalsNotes/WKProcessPool/_maximumSuspendedPageCount()``

Back/Forward キャッシュの最大ページ数を返す。

## Objective-C Declaration
```objective-c
- (NSUInteger)_maximumSuspendedPageCount WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`_processPool->backForwardCache().capacity()` を返す。

## References
- [`WKProcessPoolPrivate.h#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L146)
- [`WKProcessPool.mm#L503`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L503)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
