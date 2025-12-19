# ``WKInternalsNotes/WKWebView/_doAfterNextPresentationUpdateWithoutWaitingForPainting(_:)``

`_doAfterNextPresentationUpdateWithoutWaitingForPainting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterNextPresentationUpdateWithoutWaitingForPainting:(void (^)(void))updateBlock WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L320)
- [`API/Cocoa/WKWebView.mm#L6151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6151)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
