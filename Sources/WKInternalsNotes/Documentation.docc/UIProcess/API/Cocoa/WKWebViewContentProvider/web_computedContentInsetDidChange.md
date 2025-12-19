# ``WKInternalsNotes/WKWebViewContentProvider/web_computedContentInsetDidChange()``

計算済み content inset の変更を通知する。

## Objective-C Declaration
```objective-c
- (void)web_computedContentInsetDidChange;
```

## Discussion
`WKUSDPreviewView` では `_layoutThumbnailView` を呼び、サムネイルのレイアウトを更新する。

## References
- [`WKWebViewContentProvider.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L45)
- [`WKUSDPreviewView.mm#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L186)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
