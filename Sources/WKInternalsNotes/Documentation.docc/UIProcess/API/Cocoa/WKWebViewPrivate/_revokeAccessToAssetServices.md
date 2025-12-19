# ``WKInternalsNotes/WKWebView/_revokeAccessToAssetServices()``

`_revokeAccessToAssetServices` を実行する。

## Objective-C Declaration
```objective-c
- (void)_revokeAccessToAssetServices WK_API_AVAILABLE(macos(12.0), ios(14.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L495`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L495)
- [`WKWebView.mm#L4750`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4750)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
