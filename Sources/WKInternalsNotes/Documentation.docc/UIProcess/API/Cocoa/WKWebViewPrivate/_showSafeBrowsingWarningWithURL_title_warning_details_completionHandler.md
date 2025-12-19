# ``WKInternalsNotes/WKWebView/_showSafeBrowsingWarningWithURL(_:title:warning:details:completionHandler:)``

`_showSafeBrowsingWarningWithURL` を表示する。

## Objective-C Declaration
```objective-c
- (void)_showSafeBrowsingWarningWithURL:(NSURL *)url title:(NSString *)title warning:(NSString *)warning details:(NSAttributedString *)details completionHandler:(void(^)(BOOL))completionHandler WK_API_DEPRECATED_WITH_REPLACEMENT("-_showSafeBrowsingWarningWithURL:title:warning:detailsWithLinks:completionHandler:", macos(10.14.4, 10.15.4), ios(12.2, 13.2));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L316`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L316)
- [`API/Cocoa/WKWebView.mm#L5122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5122)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
