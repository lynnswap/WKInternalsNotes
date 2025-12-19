# ``WKInternalsNotes/WKWebView/_webProcessIdentifier``

`_webProcessIdentifier` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) pid_t _webProcessIdentifier;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L224)
- [`API/Cocoa/WKWebView.mm#L4868`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4868)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
