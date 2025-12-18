# ``WKInternalsNotes/WKProcessPool/_prewarmedProcessIdentifiersForTesting()``

プリウォーム済み WebProcess の PID 集合を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (NSSet<NSNumber *> *)_prewarmedProcessIdentifiersForTesting WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Discussion
`prewarmedProcessIdentifiers()` を走査し、`NSNumber` の `NSSet` に変換して返す。

## References
- [`WKProcessPoolPrivate.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L132)
- [`WKProcessPool.mm#L393`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L393)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
