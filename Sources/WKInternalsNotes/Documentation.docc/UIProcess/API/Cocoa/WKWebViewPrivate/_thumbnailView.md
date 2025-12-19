# ``WKInternalsNotes/WKWebView/_thumbnailView``

`_thumbnailView` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setThumbnailView:) _WKThumbnailView *_thumbnailView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setThumbnailView:`。

## References
- [`WKWebViewPrivate.h#L868`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L868)
- [`WKWebViewMac.mm#L1852`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1852)
- [`WKWebViewMac.mm#L1852`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1852)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
