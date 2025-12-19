# ``WKInternalsNotes/WKProcessPool/_setUseSeparateServiceWorkerProcess(_:)``

Service Worker を専用プロセスで動かすかを設定する。

## Objective-C Declaration
```objective-c
- (void)_setUseSeparateServiceWorkerProcess:(BOOL)forceServiceWorkerProcess WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`WebKit::WebProcessPool::setUseSeparateServiceWorkerProcess(useSeparateServiceWorkerProcess)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L152)
- [`WKProcessPool.mm#L388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L388)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
