# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:dragDestinationActionMaskForDraggingInfo:)``

ドラッグの宛先アクションマスクを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (WKDragDestinationAction)_webView:(WKWebView *)webView dragDestinationActionMaskForDraggingInfo:(id)draggingInfo WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
macOS では `NSDraggingInfo`、iOS では drop session を渡し、delegate の戻り値を使う。

## References
- [`WKUIDelegatePrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L158)
- [`WKWebViewMac.mm#L1353`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1353)
- [`WKContentViewInteraction.mm#L10955`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10955)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
