# ``WKInternalsNotes/WKProcessPool/_setLinkedOnOrAfterEverything()``

SDK アライン動作を全て有効化する。

## Objective-C Declaration
```objective-c
+ (void)_setLinkedOnOrAfterEverything WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`enableAllSDKAlignedBehaviors()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L125)
- [`WKProcessPool.mm#L552`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L552)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
