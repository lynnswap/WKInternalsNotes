# ``WKInternalsNotes/WKWebView/_certificateChain``

`_certificateChain` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray *_certificateChain WK_API_DEPRECATED_WITH_REPLACEMENT("certificateChain", macos(10.10, 10.11), ios(8.0, 9.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L214)
- [`WKWebView.mm#L4809`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4809)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
