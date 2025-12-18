# ``WKInternalsNotes/WKProcessPool/_isMetalShaderValidationEnabledInGPUProcessForTesting()``

GPU プロセスで Metal shader validation が有効かを返す（テスト用）。

## Objective-C Declaration
```objective-c
+ (BOOL)_isMetalShaderValidationEnabledInGPUProcessForTesting WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
GPUProcessProxy singleton があれば `isMetalShaderValidationEnabledForTesting()`、無ければ `isMetalShaderValidationEnabledInNewGPUProcessesForTesting()` を返す。

## References
- [`WKProcessPoolPrivate.h#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L173)
- [`WKProcessPool.mm#L594`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L594)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
