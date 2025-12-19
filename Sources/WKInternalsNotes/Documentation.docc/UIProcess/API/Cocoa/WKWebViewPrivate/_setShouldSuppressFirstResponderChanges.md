# ``WKInternalsNotes/WKWebView/_setShouldSuppressFirstResponderChanges(_:)``

`_setShouldSuppressFirstResponderChanges` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setShouldSuppressFirstResponderChanges:(BOOL)shouldSuppress;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L876`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L876)
- [`WKWebViewMac.mm#L1884`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1884)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
