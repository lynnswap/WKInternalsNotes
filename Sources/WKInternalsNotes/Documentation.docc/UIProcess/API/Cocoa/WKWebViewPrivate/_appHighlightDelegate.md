# ``WKInternalsNotes/WKWebView/_appHighlightDelegate``

`_appHighlightDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setAppHighlightDelegate:) id <_WKAppHighlightDelegate> _appHighlightDelegate WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setAppHighlightDelegate:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L471`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L471)
- [`API/Cocoa/WKWebView.mm#L2117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2117)
- [`API/Cocoa/WKWebView.mm#L2126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2126)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
