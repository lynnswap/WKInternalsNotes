# ``WKInternalsNotes/WKWebView/_focusTextInputContext(_:placeCaretAt:completionHandler:)``

`_focusTextInputContext` を実行する。

## Objective-C Declaration
```objective-c
- (void)_focusTextInputContext:(_WKTextInputContext *)context placeCaretAt:(CGPoint)point completionHandler:(void (^)(UIResponder<UITextInput> *))completionHandler;
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivateForTestingIOS.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L69)
- [`WKWebViewTestingIOS.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L81)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
