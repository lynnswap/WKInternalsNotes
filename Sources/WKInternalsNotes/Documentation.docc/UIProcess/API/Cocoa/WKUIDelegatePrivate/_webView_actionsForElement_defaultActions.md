# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:actionsForElement:defaultActions:)``

要素に対するアクション一覧を delegate で調整する。

## Objective-C Declaration
```objective-c
- (NSArray *)_webView:(WKWebView *)webView actionsForElement:(_WKActivatedElementInfo *)element defaultActions:(NSArray<_WKElementAction *> *)defaultActions;
```

## Discussion
UIClient が delegate 実装時に呼び出し、返された配列を使う。未実装時は `defaultActions` を返す。

## References
- [`WKUIDelegatePrivate.h#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L233)
- [`UIDelegate.mm#L1649`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1649)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
