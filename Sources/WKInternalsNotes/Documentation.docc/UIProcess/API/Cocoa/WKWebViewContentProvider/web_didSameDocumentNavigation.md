# ``WKInternalsNotes/WKWebViewContentProvider/web_didSameDocumentNavigation(_:)``

同一ドキュメント内のナビゲーションを通知する。

## Objective-C Declaration
```objective-c
- (void)web_didSameDocumentNavigation:(WKSameDocumentNavigationType)navigationType;
```

## Discussion
`WKUSDPreviewView` の実装は空で、特別な処理を行わない。

## References
- [`WKWebViewContentProvider.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L47)
- [`WKUSDPreviewView.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L195)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
