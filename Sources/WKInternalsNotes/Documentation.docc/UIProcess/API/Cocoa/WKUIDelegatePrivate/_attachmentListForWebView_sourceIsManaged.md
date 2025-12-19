# ``WKInternalsNotes/WKUIDelegatePrivate/_attachmentListForWebView(_:sourceIsManaged:)``

添付プレビュー用の添付リストを返し、管理対象かどうかを返す。

## Objective-C Declaration
```objective-c
- (NSArray *)_attachmentListForWebView:(WKWebView *)webView sourceIsManaged:(BOOL*)sourceIsManaged WK_API_AVAILABLE(ios(10.3));
```

## Discussion
添付プレビュー生成時に呼び出され、`sourceIsManaged` の結果が `UIPreviewDataAttachmentListIsContentManaged` に反映される。

## References
- [`WKUIDelegatePrivate.h#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L262)
- [`WKContentViewInteraction.mm#L15518`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15518)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
