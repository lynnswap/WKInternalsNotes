# ``WKInternalsNotes/WKUIDelegateInternal/_webView(_:geometryDidChange:)``

スクロールジオメトリの変更を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView geometryDidChange:(WKScrollGeometry *)geometry;
```

## Discussion
`WKWebView` の `_updateScrollGeometryWithContentOffset` で `WKScrollGeometry` を生成し、差分があれば delegate に通知する。

## References
- [`WKUIDelegateInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegateInternal.h#L34)
- [`WKWebView.mm#L3059`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3059)
- [`WKUIDelegateAdapter.swift#L147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKUIDelegateAdapter.swift#L147)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
