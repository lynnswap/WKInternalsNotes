# ``WKInternalsNotes/WKWebView/_permissionChanged(_:forOrigin:)``

`_permissionChanged` を実行する。

## Objective-C Declaration
```objective-c
+ (void)_permissionChanged:(NSString *)permissionName forOrigin:(WKSecurityOrigin *)origin WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L590`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L590)
- [`API/Cocoa/WKWebView.mm#L6256`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6256)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
