# ``WKInternalsNotes/WKProcessPool/_setLinkedOnOrBeforeEverythingForTesting()``

SDK アライン動作を全て無効化する（テスト用）。

## Objective-C Declaration
```objective-c
+ (void)_setLinkedOnOrBeforeEverythingForTesting WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`disableAllSDKAlignedBehaviors()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L165)
- [`WKProcessPool.mm#L537`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L537)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
