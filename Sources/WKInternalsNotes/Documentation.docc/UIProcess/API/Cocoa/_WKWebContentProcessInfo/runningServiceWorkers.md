# ``WKInternalsNotes/_WKWebContentProcessInfo/runningServiceWorkers``

ServiceWorker が稼働中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL runningServiceWorkers;
```

## Discussion
`WebProcessProxy::isRunningServiceWorkers()` の値を初期化時に保持する。

## References
- [`WKProcessPoolPrivate.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L67)
- [`WKProcessPool.mm#L817`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L817)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
