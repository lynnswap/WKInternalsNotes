# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:dataOwnerForDragSession:)``

Drag session の data owner を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (NSInteger)_webView:(WKWebView *)webView dataOwnerForDragSession:(id <UIDragSession>)session WK_API_AVAILABLE(ios(11.0));
```

## Discussion
delegate が応答すればその値を返し、未実装時は 0 を返す。

## References
- [`WKUIDelegatePrivate.h#L288`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L288)
- [`WKContentViewInteraction.mm#L11134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
