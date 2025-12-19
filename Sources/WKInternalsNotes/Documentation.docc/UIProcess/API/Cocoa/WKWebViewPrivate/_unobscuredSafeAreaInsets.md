# ``WKInternalsNotes/WKWebView/_unobscuredSafeAreaInsets``

`_unobscuredSafeAreaInsets` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUnobscuredSafeAreaInsets:) UIEdgeInsets _unobscuredSafeAreaInsets WK_API_AVAILABLE(ios(11.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setUnobscuredSafeAreaInsets:`。

## References
- [`WKWebViewPrivate.h#L702`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L702)
- [`WKWebViewIOS.mm#L818`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L818)
- [`WKWebViewIOS.mm#L818`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L818)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
