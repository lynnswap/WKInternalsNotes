# ``WKInternalsNotes/WKProcessPool/_setCachedProcessLifetimeForTesting(_:)``

キャッシュ済み WebProcess の寿命を設定する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_setCachedProcessLifetimeForTesting:(NSTimeInterval)lifetime WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Discussion
`webProcessCache().setCachedProcessLifetimeForTesting(Seconds { lifetime })` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L150)
- [`WKProcessPool.mm#L413`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L413)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
