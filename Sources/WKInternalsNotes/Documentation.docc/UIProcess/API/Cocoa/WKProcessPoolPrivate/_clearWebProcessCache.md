# ``WKInternalsNotes/WKProcessPool/_clearWebProcessCache()``

WebProcessCache をクリアする。

## Objective-C Declaration
```objective-c
- (void)_clearWebProcessCache WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`_processPool->webProcessCache().clear()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L150)
- [`WKProcessPool.mm#L408`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L408)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
