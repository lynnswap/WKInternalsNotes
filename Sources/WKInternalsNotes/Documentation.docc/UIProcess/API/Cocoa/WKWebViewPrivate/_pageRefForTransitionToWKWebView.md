# ``WKInternalsNotes/WKWebView/_pageRefForTransitionToWKWebView``

`_pageRefForTransitionToWKWebView` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKPageRef _pageRefForTransitionToWKWebView  WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L824`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L824)
- [`WKWebViewMac.mm#L1456`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1456)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
