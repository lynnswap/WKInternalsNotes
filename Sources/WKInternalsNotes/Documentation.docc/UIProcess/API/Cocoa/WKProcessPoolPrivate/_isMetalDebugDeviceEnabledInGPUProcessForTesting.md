# ``WKInternalsNotes/WKProcessPool/_isMetalDebugDeviceEnabledInGPUProcessForTesting()``

GPU プロセスで Metal debug device が有効かを返す（テスト用）。

## Objective-C Declaration
```objective-c
+ (BOOL)_isMetalDebugDeviceEnabledInGPUProcessForTesting WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
GPUProcessProxy singleton があれば `isMetalDebugDeviceEnabledForTesting()`、無ければ `isMetalDebugDeviceEnabledInNewGPUProcessesForTesting()` を返す。

## References
- [`WKProcessPoolPrivate.h#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L172)
- [`WKProcessPool.mm#L587`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L587)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
