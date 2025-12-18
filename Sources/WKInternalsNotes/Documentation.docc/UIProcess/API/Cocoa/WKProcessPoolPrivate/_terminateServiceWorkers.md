# ``WKInternalsNotes/WKProcessPool/_terminateServiceWorkers()``

Service Worker を終了する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_terminateServiceWorkers WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`terminateServiceWorkers()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L129)
- [`WKProcessPool.mm#L383`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L383)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
