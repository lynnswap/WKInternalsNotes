# ``WKInternalsNotes/WKWebView/_launchInitialProcessIfNecessary()``

`_launchInitialProcessIfNecessary` を実行する。

## Objective-C Declaration
```objective-c
- (void)_launchInitialProcessIfNecessary WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L305`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L305)
- [`WKWebView.mm#L5073`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5073)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
