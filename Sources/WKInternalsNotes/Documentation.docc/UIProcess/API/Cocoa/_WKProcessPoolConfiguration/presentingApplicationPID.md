# ``WKInternalsNotes/_WKProcessPoolConfiguration/presentingApplicationPID``

提示元アプリの PID を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) pid_t presentingApplicationPID WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
既定値は現在のプロセス ID。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `presentingApplicationPID` に直結し、初期値は `getCurrentProcessID()` で初期化される。

## References
- [`_WKProcessPoolConfiguration.mm#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L214)
- [`_WKProcessPoolConfiguration.mm#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L219)
- [`APIProcessPoolConfiguration.h#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
