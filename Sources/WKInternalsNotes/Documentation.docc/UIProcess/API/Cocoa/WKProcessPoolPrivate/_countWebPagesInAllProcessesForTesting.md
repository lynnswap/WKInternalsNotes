# ``WKInternalsNotes/WKProcessPool/_countWebPagesInAllProcessesForTesting(_:)``

全プロセスのページ数を非同期で取得する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_countWebPagesInAllProcessesForTesting:(void(^)(unsigned))completionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Discussion
`countWebPagesInAllProcessesForTesting` にブロックを渡し、結果を completionHandler に転送する。

## References
- [`WKProcessPoolPrivate.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L134)
- [`WKProcessPool.mm#L401`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L401)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
