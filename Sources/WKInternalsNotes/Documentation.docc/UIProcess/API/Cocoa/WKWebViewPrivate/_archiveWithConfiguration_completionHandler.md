# ``WKInternalsNotes/WKWebView/_archiveWithConfiguration(_:completionHandler:)``

`_archiveWithConfiguration` を実行する。

## Objective-C Declaration
```objective-c
- (void)_archiveWithConfiguration:(_WKArchiveConfiguration*)configuration completionHandler:(void (^)(NSError *error))completionHandler WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L359)
- [`API/Cocoa/WKWebView.mm#L5344`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5344)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
