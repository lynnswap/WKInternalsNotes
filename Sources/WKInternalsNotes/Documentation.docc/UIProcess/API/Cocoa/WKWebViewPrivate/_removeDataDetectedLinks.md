# ``WKInternalsNotes/WKWebView/_removeDataDetectedLinks(_:)``

`_removeDataDetectedLinks` を削除する。

## Objective-C Declaration
```objective-c
- (void)_removeDataDetectedLinks:(dispatch_block_t)completion WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L328`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L328)
- [`WKWebView.mm#L6129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6129)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
