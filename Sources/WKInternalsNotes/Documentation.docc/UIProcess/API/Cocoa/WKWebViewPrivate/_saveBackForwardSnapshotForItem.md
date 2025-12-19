# ``WKInternalsNotes/WKWebView/_saveBackForwardSnapshotForItem(_:)``

`_saveBackForwardSnapshotForItem` を実行する。

## Objective-C Declaration
```objective-c
- (void)_saveBackForwardSnapshotForItem:(WKBackForwardListItem *)item WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L402`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L402)
- [`WKWebView.mm#L5735`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5735)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
