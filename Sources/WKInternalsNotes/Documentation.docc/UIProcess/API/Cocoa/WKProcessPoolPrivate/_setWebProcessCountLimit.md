# ``WKInternalsNotes/WKProcessPool/_setWebProcessCountLimit(_:)``

WebProcess の上限数を設定する。

## Objective-C Declaration
```objective-c
+ (void)_setWebProcessCountLimit:(unsigned)limit WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`WebKit::WebProcessProxy::setProcessCountLimit(limit)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L109)
- [`WKProcessPool.mm#L645`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L645)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
