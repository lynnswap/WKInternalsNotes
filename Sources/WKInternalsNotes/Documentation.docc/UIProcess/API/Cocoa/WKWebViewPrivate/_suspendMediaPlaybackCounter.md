# ``WKInternalsNotes/WKWebView/_suspendMediaPlaybackCounter()``

`_suspendMediaPlaybackCounter` を実行する。

## Objective-C Declaration
```objective-c
- (NSNumber *)_suspendMediaPlaybackCounter WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L127)
- [`WKWebViewTesting.mm#L546`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L546)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
