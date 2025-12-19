# ``WKInternalsNotes/WKWebView/_preconnectToServer(_:)``

`_preconnectToServer` を実行する。

## Objective-C Declaration
```objective-c
- (void)_preconnectToServer:(NSURL *)serverURL WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L464`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L464)
- [`API/Cocoa/WKWebView.mm#L5757`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5757)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
