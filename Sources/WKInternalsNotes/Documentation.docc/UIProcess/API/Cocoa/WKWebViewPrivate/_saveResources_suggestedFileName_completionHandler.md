# ``WKInternalsNotes/WKWebView/_saveResources(_:suggestedFileName:completionHandler:)``

`_saveResources` を実行する。

## Objective-C Declaration
```objective-c
- (void)_saveResources:(NSURL *)directory suggestedFileName:(NSString *)name completionHandler:(void (^)(NSError *error))completionHandler WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L358`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L358)
- [`API/Cocoa/WKWebView.mm#L5333`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5333)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
