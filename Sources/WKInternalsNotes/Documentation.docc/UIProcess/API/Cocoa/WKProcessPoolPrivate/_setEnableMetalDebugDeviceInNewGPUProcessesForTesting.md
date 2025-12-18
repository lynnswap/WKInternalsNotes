# ``WKInternalsNotes/WKProcessPool/_setEnableMetalDebugDeviceInNewGPUProcessesForTesting(_:)``

新規 GPU プロセスで Metal debug device を有効/無効にする（テスト用）。

## Objective-C Declaration
```objective-c
+ (void)_setEnableMetalDebugDeviceInNewGPUProcessesForTesting:(BOOL)enable WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`GPUProcessProxy::setEnableMetalDebugDeviceInNewGPUProcessesForTesting(enable)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L170)
- [`WKProcessPool.mm#L577`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L577)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
