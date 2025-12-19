# ``WKInternalsNotes/WKWebView/_safeBrowsingWarning``

`_safeBrowsingWarning` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *_safeBrowsingWarning WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L727`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L727)
- [`WKWebViewIOS.mm#L4468`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4468)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
