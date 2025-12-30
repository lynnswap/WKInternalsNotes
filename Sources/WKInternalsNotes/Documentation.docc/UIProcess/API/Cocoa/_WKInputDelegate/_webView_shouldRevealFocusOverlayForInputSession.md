# ``WKInternalsNotes/_WKInputDelegate/_webView(_:shouldRevealFocusOverlayForInputSession:)``

フォーカスオーバーレイを表示するかを問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView shouldRevealFocusOverlayForInputSession:(id <_WKFormInputSession>)inputSession WK_API_AVAILABLE(ios(12.0));
```

## Discussion
`dismissQuickboardViewControllerAndRevealFocusedFormOverlayIfNecessary:` 内で、アクションの有無や前後ノードの有無を満たす場合に呼ばれる。`YES` の場合はオーバーレイを表示し、`NO` の場合はフォーカス要素を blur する。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L11949`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11949)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
