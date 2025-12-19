# ``WKInternalsNotes/WKWebView/_dontResetTransientActivationAfterRunJavaScript``

`_dontResetTransientActivationAfterRunJavaScript` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDontResetTransientActivationAfterRunJavaScript:) BOOL _dontResetTransientActivationAfterRunJavaScript WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setDontResetTransientActivationAfterRunJavaScript:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L626`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L626)
- [`API/Cocoa/WKWebView.mm#L6333`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6333)
- [`API/Cocoa/WKWebView.mm#L6338`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6338)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
