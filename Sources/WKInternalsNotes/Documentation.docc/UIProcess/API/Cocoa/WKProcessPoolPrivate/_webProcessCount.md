# ``WKInternalsNotes/WKProcessPool/_webProcessCount()``

WebProcess の総数を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (size_t)_webProcessCount WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`_processPool->processes().size()` を返す。

## References
- [`WKProcessPoolPrivate.h#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L139)
- [`WKProcessPool.mm#L418`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L418)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
