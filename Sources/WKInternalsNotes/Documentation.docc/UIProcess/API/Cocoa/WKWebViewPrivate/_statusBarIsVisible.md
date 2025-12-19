# ``WKInternalsNotes/WKWebView/_statusBarIsVisible``

`_statusBarIsVisible` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setStatusBarIsVisible:) BOOL _statusBarIsVisible WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setStatusBarIsVisible:`。

## References
- [`WKWebViewPrivate.h#L446`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L446)
- [`WKWebView.mm#L4336`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4336)
- [`WKWebView.mm#L4336`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4336)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
