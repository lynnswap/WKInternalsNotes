# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:indexIntoAttachmentListForElement:)``

添付要素が添付リストの何番目かを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (NSUInteger)_webView:(WKWebView *)webView indexIntoAttachmentListForElement:(_WKActivatedElementInfo *)element WK_API_AVAILABLE(ios(10.3));
```

## Discussion
添付プレビューの生成時に `_WKActivatedElementInfo` を渡してインデックスを取得し、`NSNotFound` でなければ preview data に attachment list と index を格納する。

## References
- [`WKUIDelegatePrivate.h#L241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L241)
- [`WKContentViewInteraction.mm#L15514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15514)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
