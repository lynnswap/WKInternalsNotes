# ``WKInternalsNotes/WKWebView/_provisionalWebProcessIdentifier``

`_provisionalWebProcessIdentifier` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) pid_t _provisionalWebProcessIdentifier WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L225)
- [`WKWebView.mm#L4876`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4876)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
