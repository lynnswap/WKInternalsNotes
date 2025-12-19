# ``WKInternalsNotes/WKWebView/_viewScale``

`_viewScale` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setViewScale:) CGFloat _viewScale WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setViewScale:`。

## References
- [`WKWebViewPrivate.h#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L292)
- [`WKWebView.mm#L5968`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5968)
- [`WKWebView.mm#L5968`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5968)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
