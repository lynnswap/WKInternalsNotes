# ``WKInternalsNotes/WKProcessPool/_makeNextWebProcessLaunchFailForTesting()``

次の WebProcess 起動を失敗させる（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_makeNextWebProcessLaunchFailForTesting WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`_processPool->setShouldMakeNextWebProcessLaunchFailForTesting(true)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L146)
- [`WKProcessPool.mm#L457`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L457)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
