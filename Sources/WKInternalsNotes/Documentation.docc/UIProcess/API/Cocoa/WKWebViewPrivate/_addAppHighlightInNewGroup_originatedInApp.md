# ``WKInternalsNotes/WKWebView/_addAppHighlightInNewGroup(_:originatedInApp:)``

`_addAppHighlightInNewGroup` を追加する。

## Objective-C Declaration
```objective-c
- (void)_addAppHighlightInNewGroup:(BOOL)newGroup originatedInApp:(BOOL)originatedInApp WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L475`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L475)
- [`WKWebView.mm#L4533`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4533)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
