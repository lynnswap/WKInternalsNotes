# ``WKInternalsNotes/WKUIDelegatePrivate/_unfocusWebView(_:)``

WebView のフォーカス解除を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_unfocusWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIClient の `unfocus` から `_unfocusWebView` を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L317`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L317)
- [`UIDelegate.mm#L1082`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1082)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
