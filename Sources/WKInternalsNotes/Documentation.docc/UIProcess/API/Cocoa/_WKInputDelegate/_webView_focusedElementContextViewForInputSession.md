# ``WKInternalsNotes/_WKInputDelegate/_webView(_:focusedElementContextViewForInputSession:)``

入力セッションのコンテキストビューを返す。

## Objective-C Declaration
```objective-c
- (UIView *)_webView:(WKWebView *)webView focusedElementContextViewForInputSession:(id <_WKFormInputSession>)inputSession WK_API_AVAILABLE(ios(12.0));
```

## Discussion
`WKContentViewInteraction` の `inputContextViewForViewController:` から呼ばれる。delegate が未実装の場合は `nil` を返す。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L12037`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12037)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
