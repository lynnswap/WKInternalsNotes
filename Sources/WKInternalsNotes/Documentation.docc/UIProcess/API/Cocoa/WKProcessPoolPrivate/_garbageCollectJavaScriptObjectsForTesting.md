# ``WKInternalsNotes/WKProcessPool/_garbageCollectJavaScriptObjectsForTesting()``

WebProcess 内の JavaScript オブジェクトを GC する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_garbageCollectJavaScriptObjectsForTesting WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`protectedProcessPool(self)->garbageCollectJavaScriptObjects()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L187)
- [`WKProcessPool.mm#L650`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L650)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
