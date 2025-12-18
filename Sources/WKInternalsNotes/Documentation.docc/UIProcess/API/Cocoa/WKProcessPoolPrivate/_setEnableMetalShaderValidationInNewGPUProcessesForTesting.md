# ``WKInternalsNotes/WKProcessPool/_setEnableMetalShaderValidationInNewGPUProcessesForTesting(_:)``

新規 GPU プロセスで Metal shader validation を有効/無効にする（テスト用）。

## Objective-C Declaration
```objective-c
+ (void)_setEnableMetalShaderValidationInNewGPUProcessesForTesting:(BOOL)enable WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`GPUProcessProxy::setEnableMetalShaderValidationInNewGPUProcessesForTesting(enable)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L171)
- [`WKProcessPool.mm#L582`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L582)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
