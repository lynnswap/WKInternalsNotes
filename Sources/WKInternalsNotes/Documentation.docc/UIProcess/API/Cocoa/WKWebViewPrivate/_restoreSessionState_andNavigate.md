# ``WKInternalsNotes/WKWebView/_restoreSessionState(_:andNavigate:)``

`_restoreSessionState` を実行する。

## Objective-C Declaration
```objective-c
- (WKNavigation *)_restoreSessionState:(_WKSessionState *)sessionState andNavigate:(BOOL)navigate;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L249)
- [`WKWebView.mm#L5001`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5001)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
