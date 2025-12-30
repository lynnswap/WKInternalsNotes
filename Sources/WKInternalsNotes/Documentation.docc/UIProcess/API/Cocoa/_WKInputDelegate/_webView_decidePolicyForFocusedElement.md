# ``WKInternalsNotes/_WKInputDelegate/_webView(_:decidePolicyForFocusedElement:)``

フォーカス開始時の入力セッションポリシーを決定する。

## Objective-C Declaration
```objective-c
- (_WKFocusStartsInputSessionPolicy)_webView:(WKWebView *)webView decidePolicyForFocusedElement:(id <_WKFocusedElementInfo>)info WK_API_AVAILABLE(ios(12.0));
```

## Discussion
`WKContentViewInteraction` のフォーカス処理で呼ばれ、返り値が `startInputSessionPolicy` を上書きする。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L8376`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8376)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
