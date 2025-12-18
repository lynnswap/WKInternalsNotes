# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:willUpdateDataInteractionOperationToOperation:forSession:)``

データインタラクションのドロップ操作種別を delegate に更新させる。

## Objective-C Declaration
```objective-c
- (NSUInteger)_webView:(WKWebView *)webView willUpdateDataInteractionOperationToOperation:(NSUInteger)operation forSession:(id)session WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKContentViewInteraction が現在の drag operation から算出した値を渡し、返った値で `UIDropProposal` を生成する。

## References
- [`WKUIDelegatePrivate.h#L281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L281)
- [`WKContentViewInteraction.mm#L11386`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11386)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
