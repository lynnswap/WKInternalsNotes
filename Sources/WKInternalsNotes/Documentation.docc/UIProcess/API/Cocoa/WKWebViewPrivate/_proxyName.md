# ``WKInternalsNotes/WKWebView/_proxyName``

`_proxyName` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *_proxyName WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L177)
- [`API/Cocoa/WKWebView.mm#L3836`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3836)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
