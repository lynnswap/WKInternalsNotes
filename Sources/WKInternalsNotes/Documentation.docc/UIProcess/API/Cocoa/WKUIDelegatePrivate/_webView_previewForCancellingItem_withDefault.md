# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:previewForCancellingItem:withDefault:)``

ドラッグキャンセル時のプレビューを delegate で上書きする。

## Objective-C Declaration
```objective-c
- (UITargetedDragPreview *)_webView:(WKWebView *)webView previewForCancellingItem:(UIDragItem *)item withDefault:(UITargetedDragPreview *)defaultPreview WK_API_AVAILABLE(ios(11.0));
```

## Discussion
delegate が `UITargetedDragPreview` を返した場合はそれを採用し、`nil` なら `_dragDropInteractionState.previewForCancelling` を使う。

## References
- [`WKUIDelegatePrivate.h#L264`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L264)
- [`WKContentViewInteraction.mm#L11260`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11260)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
