# ``WKInternalsNotes/WKWebView/_alwaysShowsHorizontalScroller``

`_alwaysShowsHorizontalScroller` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAlwaysShowsHorizontalScroller:) BOOL _alwaysShowsHorizontalScroller WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setAlwaysShowsHorizontalScroller:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L859`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L859)
- [`API/mac/WKWebViewMac.mm#L1781`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1781)
- [`API/mac/WKWebViewMac.mm#L1786`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1786)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
