# ``WKInternalsNotes/_WKInputDelegate/_webView(_:focusRequiresStrongPasswordAssistance:completionHandler:)``

フォーカス要素が強力パスワード支援を必要とするかを非同期で判定する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView focusRequiresStrongPasswordAssistance:(id <_WKFocusedElementInfo>)info completionHandler:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(ios(26.0));
```

## Discussion
`WKContentViewInteraction` のフォーカス処理で、同期版が未実装の場合に呼ばれる。`CompletionHandlerCallChecker` で `completionHandler` の呼び出しを監視し、結果を `_continueElementDidFocus` に渡す。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L8464`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8464)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
