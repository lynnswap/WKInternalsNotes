# ``WKInternalsNotes/WKWebView/_contentVisibleRect``

`_contentVisibleRect` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect _contentVisibleRect WK_API_AVAILABLE(ios(10.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L689`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L689)
- [`WKWebViewIOS.mm#L4290`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4290)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
