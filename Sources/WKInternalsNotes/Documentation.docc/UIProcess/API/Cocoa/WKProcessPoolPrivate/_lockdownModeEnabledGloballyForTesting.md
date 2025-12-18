# ``WKInternalsNotes/WKProcessPool/_lockdownModeEnabledGloballyForTesting()``

システムのロックダウンモード有効状態を返す（テスト用）。

## Objective-C Declaration
```objective-c
+ (BOOL)_lockdownModeEnabledGloballyForTesting WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`WebKit::lockdownModeEnabledBySystem()` を返す。

## References
- [`WKProcessPoolPrivate.h#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L167)
- [`WKProcessPool.mm#L567`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L567)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
