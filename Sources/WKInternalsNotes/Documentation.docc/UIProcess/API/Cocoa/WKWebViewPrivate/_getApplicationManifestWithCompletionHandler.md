# ``WKInternalsNotes/WKWebView/_getApplicationManifestWithCompletionHandler(_:)``

`_getApplicationManifestWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getApplicationManifestWithCompletionHandler:(void (^)(_WKApplicationManifest *))completionHandler WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L369`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L369)
- [`WKWebView.mm#L5493`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5493)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
