# ``WKInternalsNotes/WKWebView/_requiredWebExtensionBaseURL``

`_requiredWebExtensionBaseURL` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *_requiredWebExtensionBaseURL WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L617`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L617)
- [`API/Cocoa/WKWebView.mm#L6265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6265)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
