# ``WKInternalsNotes/WKWebView/_requestRectForFoundTextRange(_:completionHandler:)``

`_requestRectForFoundTextRange` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestRectForFoundTextRange:(UITextRange *)ranges completionHandler:(void (^)(CGRect))completionHandler WK_API_AVAILABLE(ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L681`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L681)
- [`API/ios/WKWebViewIOS.mm#L5136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5136)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
