# ``WKInternalsNotes/WKProcessPool/_isWebProcessSuspended(_:)``

指定 PID の WebProcess がサスペンド中かを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_isWebProcessSuspended:(pid_t)pid;
```

## Discussion
`_processPool->processes()` を走査し、pid が一致したら `process->throttler().isSuspended()` を返す。見つからなければ NO を返す。

## References
- [`WKProcessPoolPrivate.h#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L156)
- [`WKProcessPool.mm#L448`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L448)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
