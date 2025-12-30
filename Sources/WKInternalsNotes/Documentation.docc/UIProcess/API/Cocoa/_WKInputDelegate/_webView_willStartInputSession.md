# ``WKInternalsNotes/_WKInputDelegate/_webView(_:willStartInputSession:)``

入力セッション開始直前に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willStartInputSession:(id <_WKFormInputSession>)inputSession WK_API_AVAILABLE(ios(12.0));
```

## Discussion
`WKContentViewInteraction` の `_continueElementDidFocus` で `WKFormInputSession` を生成した後、delegate が実装していれば呼ばれる。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L8518`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8518)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
