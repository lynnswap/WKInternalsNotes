# ``WKInternalsNotes/WKProcessPool/_setDomainRelaxationForbiddenForURLScheme(_:)``

指定 scheme でドメイン緩和を禁止する。

## Objective-C Declaration
```objective-c
- (void)_setDomainRelaxationForbiddenForURLScheme:(NSString *)scheme WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`setDomainRelaxationForbiddenForURLScheme(scheme)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L123)
- [`WKProcessPool.mm#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L248)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
