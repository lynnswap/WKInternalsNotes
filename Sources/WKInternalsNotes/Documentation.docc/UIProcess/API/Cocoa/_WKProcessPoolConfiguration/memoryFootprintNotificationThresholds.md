# ``WKInternalsNotes/_WKProcessPoolConfiguration/memoryFootprintNotificationThresholds``

メモリ使用量通知のしきい値一覧を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<NSNumber *> *memoryFootprintNotificationThresholds WK_API_AVAILABLE(macos(14.5));
```

## Default Value
未設定時は空配列を返す。

## Discussion
getter は `memoryFootprintNotificationThresholds` の数値配列を `NSArray` に変換して返し、setter は `NSNumber` 配列を `Vector<uint64_t>` に変換して保存する。

## References
- [`_WKProcessPoolConfiguration.mm#L392`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L392)
- [`_WKProcessPoolConfiguration.mm#L401`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L401)
- [`APIProcessPoolConfiguration.h#L216`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L216)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
