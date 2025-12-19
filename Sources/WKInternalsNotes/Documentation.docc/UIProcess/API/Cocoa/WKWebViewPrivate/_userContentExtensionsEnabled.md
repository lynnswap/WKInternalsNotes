# ``WKInternalsNotes/WKWebView/_userContentExtensionsEnabled``

`_userContentExtensionsEnabled` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUserContentExtensionsEnabled:) BOOL _userContentExtensionsEnabled WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setUserContentExtensionsEnabled:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L222)
- [`API/Cocoa/WKWebView.mm#L4862`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4862)
- [`API/Cocoa/WKWebView.mm#L4857`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4857)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
