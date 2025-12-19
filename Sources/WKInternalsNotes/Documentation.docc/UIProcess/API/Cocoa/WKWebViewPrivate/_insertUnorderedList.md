# ``WKInternalsNotes/WKWebView/_insertUnorderedList(_:)``

`_insertUnorderedList` を実行する。

## Objective-C Declaration
```objective-c
- (IBAction)_insertUnorderedList:(id)sender WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
iOS では `WKContentViewInteraction` 側のハンドラに委譲される。

## References
- [`WKWebViewPrivate.h#L338`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L338)
- [`WKContentViewInteraction.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
