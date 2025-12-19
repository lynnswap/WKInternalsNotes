# ``WKInternalsNotes/WKWebView/_resourceLoadDelegate``

`_resourceLoadDelegate` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setResourceLoadDelegate:) id <_WKResourceLoadDelegate> _resourceLoadDelegate WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setResourceLoadDelegate:`。

## References
- [`WKWebViewPrivate.h#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L187)
- [`WKWebView.mm#L697`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L697)
- [`WKWebView.mm#L697`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L697)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
