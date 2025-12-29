# ``WKInternalsNotes/_WKProcessPoolConfiguration/alwaysKeepAndReuseSwappedProcesses``

プロセススワップ後に旧プロセスを保持して再利用するかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL alwaysKeepAndReuseSwappedProcesses WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `alwaysKeepAndReuseSwappedProcesses` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L271`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L271)
- [`_WKProcessPoolConfiguration.mm#L268`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L268)
- [`APIProcessPoolConfiguration.h#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L190)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
