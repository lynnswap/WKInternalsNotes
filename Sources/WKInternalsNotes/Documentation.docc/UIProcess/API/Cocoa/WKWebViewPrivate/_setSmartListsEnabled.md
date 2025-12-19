# ``WKInternalsNotes/WKWebView/_setSmartListsEnabled(_:)``

`_setSmartListsEnabled` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setSmartListsEnabled:(BOOL)flag WK_API_AVAILABLE(macos(WK_MAC_TBA));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L936`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L936)
- [`WKWebViewMac.mm#L2065`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L2065)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
