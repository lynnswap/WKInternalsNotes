# ``WKInternalsNotes/WKWebView/_callAsyncJavaScript(_:arguments:inFrame:inContentWorld:completionHandler:)``

`_callAsyncJavaScript` を実行する。

## Objective-C Declaration
```objective-c
- (void)_callAsyncJavaScript:(NSString *)functionBody arguments:(NSDictionary<NSString *, id> *)arguments inFrame:(WKFrameInfo *)frame inContentWorld:(WKContentWorld *)contentWorld completionHandler:(void (^)(id, NSError *error))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L282`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L282)
- [`WKWebView.mm#L5187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
