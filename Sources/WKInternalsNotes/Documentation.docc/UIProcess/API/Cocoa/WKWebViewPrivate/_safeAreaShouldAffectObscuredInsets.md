# ``WKInternalsNotes/WKWebView/_safeAreaShouldAffectObscuredInsets``

`_safeAreaShouldAffectObscuredInsets` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _safeAreaShouldAffectObscuredInsets WK_API_AVAILABLE(ios(11.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L703`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L703)
- [`WKWebViewIOS.mm#L789`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L789)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
