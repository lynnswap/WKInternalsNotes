# ``WKInternalsNotes/WKProcessPool/_setLinkedOnOrAfterEverythingForTesting()``

SDK アライン動作を全て有効化する（テスト用）。

## Objective-C Declaration
```objective-c
+ (void)_setLinkedOnOrAfterEverythingForTesting WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`_setLinkedOnOrAfterEverything` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L163)
- [`WKProcessPool.mm#L542`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L542)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
