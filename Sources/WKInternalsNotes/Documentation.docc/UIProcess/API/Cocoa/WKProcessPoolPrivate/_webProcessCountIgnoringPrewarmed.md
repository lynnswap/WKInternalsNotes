# ``WKInternalsNotes/WKProcessPool/_webProcessCountIgnoringPrewarmed()``

プリウォーム済みを除いた WebProcess 数を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (size_t)_webProcessCountIgnoringPrewarmed WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`_webProcessCount` から `_hasPrewarmedWebProcess` が true の場合に 1 を引いて返す。

## References
- [`WKProcessPoolPrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L141)
- [`WKProcessPool.mm#L471`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L471)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
