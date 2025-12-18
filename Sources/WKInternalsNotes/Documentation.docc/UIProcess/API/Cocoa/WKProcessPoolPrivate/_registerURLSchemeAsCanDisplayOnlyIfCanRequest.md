# ``WKInternalsNotes/WKProcessPool/_registerURLSchemeAsCanDisplayOnlyIfCanRequest(_:)``

要求可能な場合のみ表示可能な URL scheme を登録する。

## Objective-C Declaration
```objective-c
- (void)_registerURLSchemeAsCanDisplayOnlyIfCanRequest:(NSString *)scheme WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`registerURLSchemeAsCanDisplayOnlyIfCanRequest(scheme)` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L119)
- [`WKProcessPool.mm#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L233)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
