# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:willSnapshotBackForwardListItem:)``

履歴項目のスナップショット取得を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willSnapshotBackForwardListItem:(WKBackForwardListItem *)item;
```

## Discussion
willRecordNavigationSnapshot で BackForwardListItem をラップして呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L72)
- [`NavigationState.mm#L206`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L206)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
