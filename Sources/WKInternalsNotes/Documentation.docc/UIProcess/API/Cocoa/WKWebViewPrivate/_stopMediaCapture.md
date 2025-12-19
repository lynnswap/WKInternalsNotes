# ``WKInternalsNotes/WKWebView/_stopMediaCapture()``

`_stopMediaCapture` を終了する。

## Objective-C Declaration
```objective-c
- (void)_stopMediaCapture WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L415`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L415)
- [`WKWebView.mm#L4468`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4468)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
