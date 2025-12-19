# ``WKInternalsNotes/WKWebView/_uiEventAttribution``

`_uiEventAttribution` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setUIEventAttribution:) UIEventAttribution *_uiEventAttribution WK_API_AVAILABLE(ios(15.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setUIEventAttribution:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L671`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L671)
- [`API/ios/WKWebViewIOS.mm#L4245`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4245)
- [`API/ios/WKWebViewIOS.mm#L4227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4227)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
