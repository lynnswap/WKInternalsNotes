# ``WKInternalsNotes/WKWebView/presentingApplicationAuditToken``

`presentingApplicationAuditToken` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) audit_token_t presentingApplicationAuditToken WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `setPresentingApplicationAuditToken:`。

## References
- [`WKWebViewPrivate.h#L638`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L638)
- [`WKWebView.mm#L6440`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6440)
- [`WKWebView.mm#L6440`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6440)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
