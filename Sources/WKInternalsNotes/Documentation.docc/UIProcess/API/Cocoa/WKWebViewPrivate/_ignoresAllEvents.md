# ``WKInternalsNotes/WKWebView/_ignoresAllEvents``

`_ignoresAllEvents` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setIgnoresAllEvents:) BOOL _ignoresAllEvents WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setIgnoresAllEvents:`。

## References
- [`WKWebViewPrivate.h#L869`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L869)
- [`WKWebViewMac.mm#L1865`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1865)
- [`WKWebViewMac.mm#L1865`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1865)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
