# ``WKInternalsNotes/WKProcessPool/_gpuProcessIdentifier()``

GPU プロセスの PID を返す。

## Objective-C Declaration
```objective-c
- (pid_t)_gpuProcessIdentifier WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
GPU プロセスが存在すれば `processID()` を返し、存在しなければ 0（`ENABLE(GPU_PROCESS)` 無効時も 0）。

## References
- [`WKProcessPoolPrivate.h#L153`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L153)
- [`WKProcessPool.mm#L423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
