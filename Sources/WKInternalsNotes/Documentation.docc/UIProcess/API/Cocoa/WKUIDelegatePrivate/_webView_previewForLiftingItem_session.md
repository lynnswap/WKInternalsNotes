# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:previewForLiftingItem:session:)``

ドラッグ開始時のリフトプレビューを delegate で上書きする。

## Objective-C Declaration
```objective-c
- (UITargetedDragPreview *)_webView:(WKWebView *)webView previewForLiftingItem:(UIDragItem *)item session:(id <UIDragSession>)session WK_API_AVAILABLE(ios(11.0));
```

## Discussion
delegate が `UITargetedDragPreview` を返した場合はそれを採用し、`nil` なら `_dragDropInteractionState.previewForLifting` を使う。

## References
- [`WKUIDelegatePrivate.h#L261`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L261)
- [`WKContentViewInteraction.mm#L11217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11217)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
