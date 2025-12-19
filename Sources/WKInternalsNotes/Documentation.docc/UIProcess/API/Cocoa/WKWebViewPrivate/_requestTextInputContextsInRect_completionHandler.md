# ``WKInternalsNotes/WKWebView/_requestTextInputContextsInRect(_:completionHandler:)``

`_requestTextInputContextsInRect` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestTextInputContextsInRect:(CGRect)rect completionHandler:(void (^)(NSArray<_WKTextInputContext *> *))completionHandler;
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/ios/WKWebViewPrivateForTestingIOS.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L68)
- [`API/ios/WKWebViewTestingIOS.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
