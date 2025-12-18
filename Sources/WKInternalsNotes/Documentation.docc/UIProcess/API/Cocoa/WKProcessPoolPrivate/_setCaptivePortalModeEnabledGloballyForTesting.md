# ``WKInternalsNotes/WKProcessPool/_setCaptivePortalModeEnabledGloballyForTesting(_:)``

ロックダウンモードのテスト設定を有効/無効にする。

## Objective-C Declaration
```objective-c
+ (void)_setCaptivePortalModeEnabledGloballyForTesting:(BOOL)isEnabled WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`WebKit::setLockdownModeEnabledGloballyForTesting(!!isEnabled)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L165)
- [`WKProcessPool.mm#L562`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L562)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
