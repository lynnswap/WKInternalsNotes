# ``WKInternalsNotes/WKProcessPool/_serviceWorkerProcessCount()``

Service Worker プロセス数を返す。

## Objective-C Declaration
```objective-c
- (size_t)_serviceWorkerProcessCount WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`serviceWorkerProxiesCount()` を返す。

## References
- [`WKProcessPoolPrivate.h#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L143)
- [`WKProcessPool.mm#L518`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L518)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
