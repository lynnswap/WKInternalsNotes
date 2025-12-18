# ``WKInternalsNotes/WKUIDelegatePrivate/_attachmentListForWebView(_:)``

添付プレビュー用の添付リストを返す。

## Objective-C Declaration
```objective-c
- (NSArray *)_attachmentListForWebView:(WKWebView *)webView WK_API_AVAILABLE(ios(10.0));
```

## Discussion
添付プレビュー生成時に `UIPreviewDataAttachmentList` へ設定する配列として呼び出される。

## References
- [`WKUIDelegatePrivate.h#L261`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L261)
- [`WKContentViewInteraction.mm#L15588`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15588)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
