# ``WKInternalsNotes/WKWebView/_requestActiveNowPlayingSessionInfo(_:)``

`_requestActiveNowPlayingSessionInfo` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestActiveNowPlayingSessionInfo:(void(^)(BOOL, BOOL, NSString*, double, double, NSInteger))callback;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L69)
- [`WKWebViewTesting.mm#L271`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L271)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
