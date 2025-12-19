# ``WKInternalsNotes/WKContentView/initWithFrame(_:processPool:configuration:webView:)``

WKContentView を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame processPool:(std::reference_wrapper<WebKit::WebProcessPool>)processPool configuration:(Ref<API::PageConfiguration>&&)configuration webView:(WKWebView *)webView;
```

## Discussion
`WKWebView` を使って superclass を初期化し、`PageClientImpl` を構築した上で `_commonInitializationWithProcessPool:configuration:` を呼び出す。

## References
- [`WKContentView.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L72)
- [`WKContentView.mm#L484`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L484)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
