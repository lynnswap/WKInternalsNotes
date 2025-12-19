# ``WKInternalsNotes/WKWebView/_negotiatedLegacyTLS``

`_negotiatedLegacyTLS` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _negotiatedLegacyTLS WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L236)
- [`API/Cocoa/WKWebView.mm#L3826`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3826)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
