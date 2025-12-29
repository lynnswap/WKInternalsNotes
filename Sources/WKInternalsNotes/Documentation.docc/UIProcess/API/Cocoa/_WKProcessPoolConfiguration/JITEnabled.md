# ``WKInternalsNotes/_WKProcessPoolConfiguration/JITEnabled``

WebContent プロセスの JIT を有効/無効にする。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isJITEnabled) BOOL JITEnabled WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
既定値は `true`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `isJITEnabled`/`setJITEnabled` に直結し、JIT の使用可否を切り替える。

## References
- [`_WKProcessPoolConfiguration.mm#L306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L306)
- [`_WKProcessPoolConfiguration.mm#L311`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L311)
- [`APIProcessPoolConfiguration.h#L197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L197)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
