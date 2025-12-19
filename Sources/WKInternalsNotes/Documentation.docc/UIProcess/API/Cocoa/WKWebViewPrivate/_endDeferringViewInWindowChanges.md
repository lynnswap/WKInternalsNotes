# ``WKInternalsNotes/WKWebView/_endDeferringViewInWindowChanges()``

`_endDeferringViewInWindowChanges` を終了する。

## Objective-C Declaration
```objective-c
- (void)_endDeferringViewInWindowChanges WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L889`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L889)
- [`API/mac/WKWebViewMac.mm#L1936`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1936)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
