# ``WKInternalsNotes/WKWebView/_applicationNameForUserAgent``

`_applicationNameForUserAgent` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (copy, setter=_setApplicationNameForUserAgent:) NSString *_applicationNameForUserAgent;
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setApplicationNameForUserAgent:`。

## References
- [`WKWebViewPrivate.h#L218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L218)
- [`WKWebView.mm#L4835`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4835)
- [`WKWebView.mm#L4835`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4835)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
