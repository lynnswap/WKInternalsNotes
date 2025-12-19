# ``WKInternalsNotes/WKWebView/_obscuredContentInsets``

`_obscuredContentInsets` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSEdgeInsets _obscuredContentInsets WK_API_AVAILABLE(macos(26.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L923`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L923)
- [`API/mac/WKWebViewMac.mm#L1603`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1603)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
