# ``WKInternalsNotes/WKContentView/becomeFirstResponderForWebView()``

WebView の first responder 取得を行う。

## Objective-C Declaration
```objective-c
- (BOOL)becomeFirstResponderForWebView;
```

## Discussion
`_resigningFirstResponder` 中なら `NO`。それ以外は入力ビュー更新を遅延しつつ `super` の `becomeFirstResponder` を呼び、成功時は activity state 更新や選択の再活性化を行う。

## References
- [`WKContentViewInteraction.h#L758`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L758)
- [`WKContentViewInteraction.mm#L2001`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2001)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
