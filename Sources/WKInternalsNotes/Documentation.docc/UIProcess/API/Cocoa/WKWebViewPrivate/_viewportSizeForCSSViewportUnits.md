# ``WKInternalsNotes/WKWebView/_viewportSizeForCSSViewportUnits``

`_viewportSizeForCSSViewportUnits` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setViewportSizeForCSSViewportUnits:) CGSize _viewportSizeForCSSViewportUnits WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setViewportSizeForCSSViewportUnits:`。

## References
- [`WKWebViewPrivate.h#L290`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L290)
- [`WKWebView.mm#L3771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3771)
- [`WKWebView.mm#L3771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3771)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
