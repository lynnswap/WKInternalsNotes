# ``WKInternalsNotes/WKWebView/_useSystemAppearance``

`_useSystemAppearance` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setUseSystemAppearance:) BOOL _useSystemAppearance WK_API_AVAILABLE(macos(10.14), ios(18.4), visionos(2.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setUseSystemAppearance:`。

## References
- [`WKWebViewPrivate.h#L298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L298)
- [`WKWebView.mm#L6450`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6450)
- [`WKWebView.mm#L6450`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6450)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
