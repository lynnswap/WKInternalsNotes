# ``WKInternalsNotes/WKProcessPool/_hasPrewarmedWebProcess()``

プリウォームされた WebProcess が存在するかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_hasPrewarmedWebProcess WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`_processPool->processes()` を走査し、`isPrewarmed()` があれば YES を返す。

## References
- [`WKProcessPoolPrivate.h#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L139)
- [`WKProcessPool.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L462)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
