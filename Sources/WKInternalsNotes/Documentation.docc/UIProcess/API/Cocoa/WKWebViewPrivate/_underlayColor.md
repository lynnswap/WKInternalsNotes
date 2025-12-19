# ``WKInternalsNotes/WKWebView/_underlayColor``

`_underlayColor` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setUnderlayColor:) NSColor *_underlayColor WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setUnderlayColor:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L840`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L840)
- [`API/mac/WKWebViewMac.mm#L1537`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1537)
- [`API/mac/WKWebViewMac.mm#L1542`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1542)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
