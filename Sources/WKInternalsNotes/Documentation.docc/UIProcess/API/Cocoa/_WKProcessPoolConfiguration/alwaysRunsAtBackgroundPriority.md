# ``WKInternalsNotes/_WKProcessPoolConfiguration/alwaysRunsAtBackgroundPriority``

iOS で WebContent プロセスを常にバックグラウンド優先度で動かすかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL alwaysRunsAtBackgroundPriority WK_API_AVAILABLE(ios(10.3));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `alwaysRunsAtBackgroundPriority` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L317`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L317)
- [`_WKProcessPoolConfiguration.mm#L322`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L322)
- [`APIProcessPoolConfiguration.h#L184`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L184)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
