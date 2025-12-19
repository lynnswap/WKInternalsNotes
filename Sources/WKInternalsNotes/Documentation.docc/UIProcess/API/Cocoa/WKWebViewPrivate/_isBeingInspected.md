# ``WKInternalsNotes/WKWebView/_isBeingInspected``

`_isBeingInspected` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isBeingInspected WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L254)
- [`WKWebView.mm#L3786`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3786)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
