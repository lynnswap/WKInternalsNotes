# ``WKInternalsNotes/WKProcessPool/_preconnectToServer(_:)``

指定サーバーへのプリコネクトを要求する。

## Objective-C Declaration
```objective-c
- (void)_preconnectToServer:(NSURL *)serverURL WK_API_DEPRECATED_WITH_REPLACEMENT("WKWebView._preconnectToServer", macos(10.13.4, 10.15.4), ios(11.3, 13.4));
```

## Discussion
現在の実装は空で、処理は行わない。

## References
- [`WKProcessPoolPrivate.h#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L176)
- [`WKProcessPool.mm#L494`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L494)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
