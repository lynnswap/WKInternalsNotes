# ``WKInternalsNotes/_WKInputDelegate/_webView(_:focusRequiresStrongPasswordAssistance:)``

フォーカス要素が強力パスワード支援を必要とするかを同期で判定する。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView focusRequiresStrongPasswordAssistance:(id <_WKFocusedElementInfo>)info WK_API_AVAILABLE(ios(12.0));
```

## Discussion
`WKContentViewInteraction` のフォーカス処理で呼ばれ、返り値が `_continueElementDidFocus` に渡される。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L8458`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8458)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
