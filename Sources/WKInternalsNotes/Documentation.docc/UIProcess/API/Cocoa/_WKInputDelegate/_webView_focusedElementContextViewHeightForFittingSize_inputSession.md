# ``WKInternalsNotes/_WKInputDelegate/_webView(_:focusedElementContextViewHeightForFittingSize:inputSession:)``

入力セッションのコンテキストビュー高さを返す。

## Objective-C Declaration
```objective-c
- (CGFloat)_webView:(WKWebView *)webView focusedElementContextViewHeightForFittingSize:(CGSize)fittingSize inputSession:(id <_WKFormInputSession>)inputSession WK_API_AVAILABLE(ios(12.0));
```

## Discussion
UIProcess 配下の `.m/.mm` では呼び出しが見当たらず、使用箇所は確認できていない。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
