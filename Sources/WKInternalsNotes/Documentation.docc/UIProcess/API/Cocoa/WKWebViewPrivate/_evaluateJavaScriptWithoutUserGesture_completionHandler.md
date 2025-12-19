# ``WKInternalsNotes/WKWebView/_evaluateJavaScriptWithoutUserGesture(_:completionHandler:)``

`_evaluateJavaScriptWithoutUserGesture` を実行する。

## Objective-C Declaration
```objective-c
- (void)_evaluateJavaScriptWithoutUserGesture:(NSString *)javaScriptString completionHandler:(void (^)(id, NSError *))completionHandler WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L278`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L278)
- [`API/Cocoa/WKWebView.mm#L5181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5181)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
