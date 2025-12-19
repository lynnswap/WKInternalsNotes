# ``WKInternalsNotes/WKWebView/_pasteAsQuotation(_:)``

`_pasteAsQuotation` を実行する。

## Objective-C Declaration
```objective-c
- (IBAction)_pasteAsQuotation:(id)sender WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
iOS では `WKContentViewInteraction` 側のハンドラに委譲される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L344`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L344)
- [`ios/WKContentViewInteraction.mm#L4990`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4990)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
