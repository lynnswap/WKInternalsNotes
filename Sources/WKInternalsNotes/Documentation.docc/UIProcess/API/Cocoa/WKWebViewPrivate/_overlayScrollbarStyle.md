# ``WKInternalsNotes/WKWebView/_overlayScrollbarStyle``

`_overlayScrollbarStyle` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOverlayScrollbarStyle:) _WKOverlayScrollbarStyle _overlayScrollbarStyle WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setOverlayScrollbarStyle:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L862`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L862)
- [`API/mac/WKWebViewMac.mm#L1806`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1806)
- [`API/mac/WKWebViewMac.mm#L1801`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1801)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
