# ``WKInternalsNotes/_WKWebContentProcessInfo/runningSharedWorkers``

SharedWorker が稼働中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL runningSharedWorkers;
```

## Discussion
`WebProcessProxy::isRunningSharedWorkers()` の値を初期化時に保持する。

## References
- [`WKProcessPoolPrivate.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L68)
- [`WKProcessPool.mm#L818`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L818)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
