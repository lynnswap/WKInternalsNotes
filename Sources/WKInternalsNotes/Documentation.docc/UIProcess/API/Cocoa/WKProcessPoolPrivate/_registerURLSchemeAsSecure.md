# ``WKInternalsNotes/WKProcessPool/_registerURLSchemeAsSecure(_:)``

セキュア扱いする URL scheme を登録する。

## Objective-C Declaration
```objective-c
- (void)_registerURLSchemeAsSecure:(NSString *)scheme WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`registerURLSchemeAsSecure(scheme)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L120)
- [`WKProcessPool.mm#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L238)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
