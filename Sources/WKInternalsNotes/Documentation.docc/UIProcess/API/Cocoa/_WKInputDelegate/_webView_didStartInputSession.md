# ``WKInternalsNotes/_WKInputDelegate/_webView(_:didStartInputSession:)``

入力セッション開始後に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didStartInputSession:(id <_WKFormInputSession>)inputSession;
```

## Discussion
`WKContentViewInteraction` で `_inputPeripheral` の編集開始後に呼ばれる。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L8615`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8615)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
