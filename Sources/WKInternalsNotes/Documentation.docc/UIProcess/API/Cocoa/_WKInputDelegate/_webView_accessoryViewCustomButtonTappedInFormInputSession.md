# ``WKInternalsNotes/_WKInputDelegate/_webView(_:accessoryViewCustomButtonTappedInFormInputSession:)``

フォームアクセサリのカスタムボタン押下を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView accessoryViewCustomButtonTappedInFormInputSession:(id <_WKFormInputSession>)inputSession;
```

## Discussion
`WKContentViewInteraction` の `accessoryViewAutoFill:` で呼ばれる。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L6293`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6293)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
