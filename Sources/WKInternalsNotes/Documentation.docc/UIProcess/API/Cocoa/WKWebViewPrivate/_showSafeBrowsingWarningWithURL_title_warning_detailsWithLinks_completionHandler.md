# ``WKInternalsNotes/WKWebView/_showSafeBrowsingWarningWithURL(_:title:warning:detailsWithLinks:completionHandler:)``

`_showSafeBrowsingWarningWithURL` を表示する。

## Objective-C Declaration
```objective-c
- (void)_showSafeBrowsingWarningWithURL:(NSURL *)url title:(NSString *)title warning:(NSString *)warning detailsWithLinks:(NSAttributedString *)details completionHandler:(void(^)(BOOL, NSURL *))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.2));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L315`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L315)
- [`WKWebView.mm#L5122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5122)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
