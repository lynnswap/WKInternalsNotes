# ``WKInternalsNotes/WKWebView/_evaluateJavaScript(_:inFrame:inContentWorld:completionHandler:)``

`_evaluateJavaScript` を実行する。

## Objective-C Declaration
```objective-c
- (void)_evaluateJavaScript:(NSString *)javaScriptString inFrame:(WKFrameInfo *)frame inContentWorld:(WKContentWorld *)contentWorld completionHandler:(void (^)(id, NSError * error))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L279`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L279)
- [`API/Cocoa/WKWebView.mm#L1454`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1454)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
