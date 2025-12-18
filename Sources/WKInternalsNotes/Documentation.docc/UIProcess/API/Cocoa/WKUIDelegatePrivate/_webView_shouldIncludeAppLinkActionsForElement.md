# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:shouldIncludeAppLinkActionsForElement:)``

App Link アクションを含めるか delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView shouldIncludeAppLinkActionsForElement:(_WKActivatedElementInfo *)element WK_API_AVAILABLE(ios(9.0));
```

## Discussion
UIDelegate::UIClient が delegate へ要素情報を渡し、未実装時は `true` を返す。

## References
- [`WKUIDelegatePrivate.h#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L233)
- [`UIDelegate.mm#L1632`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1632)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
