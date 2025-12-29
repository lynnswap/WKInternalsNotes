# ``WKInternalsNotes/_WKProcessPoolConfiguration/prewarmedProcessCountLimitForTesting``

テスト用にプレウォームするプロセス数の上限を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) unsigned prewarmedProcessCountLimitForTesting WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Default Value
既定値は `0`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `prewarmedProcessCountLimitForTesting` に直結する。

## References
- [`_WKProcessPoolConfiguration.mm#L426`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L426)
- [`_WKProcessPoolConfiguration.mm#L431`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L431)
- [`APIProcessPoolConfiguration.h#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L220)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
