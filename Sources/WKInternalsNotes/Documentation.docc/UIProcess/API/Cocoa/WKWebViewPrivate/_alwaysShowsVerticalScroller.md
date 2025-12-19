# ``WKInternalsNotes/WKWebView/_alwaysShowsVerticalScroller``

`_alwaysShowsVerticalScroller` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAlwaysShowsVerticalScroller:) BOOL _alwaysShowsVerticalScroller WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setAlwaysShowsVerticalScroller:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L860`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L860)
- [`API/mac/WKWebViewMac.mm#L1791`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1791)
- [`API/mac/WKWebViewMac.mm#L1796`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1796)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
