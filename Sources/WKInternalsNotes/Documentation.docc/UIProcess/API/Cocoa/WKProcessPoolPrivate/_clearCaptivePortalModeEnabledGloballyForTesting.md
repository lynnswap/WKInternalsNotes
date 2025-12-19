# ``WKInternalsNotes/WKProcessPool/_clearCaptivePortalModeEnabledGloballyForTesting()``

グローバルなロックダウンモードのテスト設定を解除する。

## Objective-C Declaration
```objective-c
+ (void)_clearCaptivePortalModeEnabledGloballyForTesting WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`WebKit::setLockdownModeEnabledGloballyForTesting(std::nullopt)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L167)
- [`WKProcessPool.mm#L572`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L572)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
