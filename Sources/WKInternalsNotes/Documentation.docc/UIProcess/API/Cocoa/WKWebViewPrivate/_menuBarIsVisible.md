# ``WKInternalsNotes/WKWebView/_menuBarIsVisible``

`_menuBarIsVisible` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMenuBarIsVisible:) BOOL _menuBarIsVisible WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setMenuBarIsVisible:`。

## References
- [`WKWebViewPrivate.h#L447`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L447)
- [`WKWebView.mm#L4346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4346)
- [`WKWebView.mm#L4346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4346)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
