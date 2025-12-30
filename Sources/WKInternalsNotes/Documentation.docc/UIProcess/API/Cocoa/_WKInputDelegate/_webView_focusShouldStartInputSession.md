# ``WKInternalsNotes/_WKInputDelegate/_webView(_:focusShouldStartInputSession:)``

入力セッションを開始すべきかを問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView focusShouldStartInputSession:(id <_WKFocusedElementInfo>)info;
```

## Discussion
`WKContentViewInteraction` のフォーカス処理で呼ばれ、返り値に応じて `_WKFocusStartsInputSessionPolicyAllow` または `_WKFocusStartsInputSessionPolicyDisallow` を設定する。後続の `decidePolicyForFocusedElement` があれば上書きされる。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L8369`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8369)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
