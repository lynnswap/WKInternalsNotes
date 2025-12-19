# ``WKInternalsNotes/WKWebView/_clipsToVisibleRect``

`_clipsToVisibleRect` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setClipsToVisibleRect:) BOOL _clipsToVisibleRect WK_API_AVAILABLE(macos(11.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setClipsToVisibleRect:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L832`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L832)
- [`API/mac/WKWebViewMac.mm#L1771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1771)
- [`API/mac/WKWebViewMac.mm#L1776`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1776)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
