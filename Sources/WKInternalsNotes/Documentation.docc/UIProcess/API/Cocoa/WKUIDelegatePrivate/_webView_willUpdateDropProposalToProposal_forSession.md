# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:willUpdateDropProposalToProposal:forSession:)``

ドロップ提案を delegate に調整させる。

## Objective-C Declaration
```objective-c
- (UIDropProposal *)_webView:(WKWebView *)webView willUpdateDropProposalToProposal:(UIDropProposal *)proposal forSession:(id <UIDropSession>)session WK_API_AVAILABLE(ios(12.2));
```

## Discussion
WKContentViewInteraction が生成した `UIDropProposal` を delegate が必要に応じて置き換える。

## References
- [`WKUIDelegatePrivate.h#L284`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L284)
- [`WKContentViewInteraction.mm#L11401`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11401)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
