# ``WKInternalsNotes/WKWebView/_customUserAgent``

`_customUserAgent` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (copy, setter=_setCustomUserAgent:) NSString *_customUserAgent;
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setCustomUserAgent:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L219)
- [`API/Cocoa/WKWebView.mm#L4847`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4847)
- [`API/Cocoa/WKWebView.mm#L4852`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4852)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
