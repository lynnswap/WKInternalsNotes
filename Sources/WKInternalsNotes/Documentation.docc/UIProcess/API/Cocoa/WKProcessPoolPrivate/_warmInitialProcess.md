# ``WKInternalsNotes/WKProcessPool/_warmInitialProcess()``

初期 WebProcess をプリウォームする。

## Objective-C Declaration
```objective-c
- (void)_warmInitialProcess WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
`prewarmProcess()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L111)
- [`WKProcessPool.mm#L338`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L338)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
