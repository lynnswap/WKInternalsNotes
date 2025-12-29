# ``WKInternalsNotes/_WKProcessPoolConfiguration/memoryFootprintPollIntervalForTesting``

メモリフットプリントのポーリング間隔（テスト用）を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSTimeInterval memoryFootprintPollIntervalForTesting;
```

## Default Value
既定値は 0 秒。

## Discussion
setter は `NSTimeInterval` を `Seconds` に変換して保存し、getter は `seconds()` を返す。

## References
- [`_WKProcessPoolConfiguration.mm#L382`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L382)
- [`_WKProcessPoolConfiguration.mm#L387`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L387)
- [`APIProcessPoolConfiguration.h#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
