# ``WKInternalsNotes/WKProcessPool/_webProcessCountIgnoringPrewarmedAndCached()``

プリウォーム/キャッシュを除いた WebProcess 数を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (size_t)_webProcessCountIgnoringPrewarmedAndCached WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`processes()` を走査して `isInProcessCache()` と `isPrewarmed()` のどちらでもないものだけを数える。

## References
- [`WKProcessPoolPrivate.h#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L142)
- [`WKProcessPool.mm#L476`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L476)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
