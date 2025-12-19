# ``WKInternalsNotes/WKWebView/_handle``

`_handle` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKBrowsingContextHandle *_handle;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L181)
- [`WKWebView.mm#L1497`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1497)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
