# ``WKInternalsNotes/WKWebView/_fullscreenDelegate``

`_fullscreenDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setFullscreenDelegate:) id<_WKFullscreenDelegate> _fullscreenDelegate WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setFullscreenDelegate:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L406`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L406)
- [`API/Cocoa/WKWebView.mm#L6075`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6075)
- [`API/Cocoa/WKWebView.mm#L6066`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6066)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
