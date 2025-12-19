# ``WKInternalsNotes/WKWebView/_drawsBackground``

`_drawsBackground` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDrawsBackground:) BOOL _drawsBackground;
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setDrawsBackground:`。

## References
- [`WKWebViewPrivate.h#L843`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L843)
- [`WKWebViewMac.mm#L1557`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1557)
- [`WKWebViewMac.mm#L1557`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1557)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
