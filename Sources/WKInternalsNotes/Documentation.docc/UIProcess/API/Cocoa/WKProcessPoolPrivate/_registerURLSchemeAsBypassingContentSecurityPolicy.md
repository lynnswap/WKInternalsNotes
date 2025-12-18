# ``WKInternalsNotes/WKProcessPool/_registerURLSchemeAsBypassingContentSecurityPolicy(_:)``

CSP をバイパスする URL scheme を登録する。

## Objective-C Declaration
```objective-c
- (void)_registerURLSchemeAsBypassingContentSecurityPolicy:(NSString *)scheme WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`registerURLSchemeAsBypassingContentSecurityPolicy(scheme)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L121)
- [`WKProcessPool.mm#L243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L243)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
