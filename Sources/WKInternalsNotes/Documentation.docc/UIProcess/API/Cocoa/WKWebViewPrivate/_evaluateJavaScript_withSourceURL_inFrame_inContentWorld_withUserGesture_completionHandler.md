# ``WKInternalsNotes/WKWebView/_evaluateJavaScript(_:withSourceURL:inFrame:inContentWorld:withUserGesture:completionHandler:)``

`_evaluateJavaScript` を実行する。

## Objective-C Declaration
```objective-c
- (void)_evaluateJavaScript:(NSString *)javaScriptString withSourceURL:(NSURL *)url inFrame:(WKFrameInfo *)frame inContentWorld:(WKContentWorld *)contentWorld withUserGesture:(BOOL)withUserGesture completionHandler:(void (^)(id, NSError *error))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L281)
- [`API/Cocoa/WKWebView.mm#L1454`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1454)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
