# ``WKInternalsNotes/_WKProcessPoolConfiguration/suspendsWebProcessesAggressivelyOnMemoryPressure``

メモリ圧迫時に WebProcess を積極的にサスペンドするかを制御する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL suspendsWebProcessesAggressivelyOnMemoryPressure WK_API_AVAILABLE(macos(15.4));
```

## Default Value
既定値は `false`。

## Discussion
`ENABLE(WEB_PROCESS_SUSPENSION_DELAY)` 有効時のみ `ProcessPoolConfiguration` に保存され、無効時は getter が `NO` を返し setter は no-op になる。

## References
- [`_WKProcessPoolConfiguration.mm#L410`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L410)
- [`_WKProcessPoolConfiguration.mm#L419`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L419)
- [`APIProcessPoolConfiguration.h#L218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L218)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
