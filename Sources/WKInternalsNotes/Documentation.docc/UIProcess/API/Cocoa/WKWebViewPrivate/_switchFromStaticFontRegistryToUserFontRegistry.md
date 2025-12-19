# ``WKInternalsNotes/WKWebView/_switchFromStaticFontRegistryToUserFontRegistry()``

`_switchFromStaticFontRegistryToUserFontRegistry` を実行する。

## Objective-C Declaration
```objective-c
- (void)_switchFromStaticFontRegistryToUserFontRegistry WK_API_AVAILABLE(macos(12.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L507`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L507)
- [`WKWebView.mm#L4764`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4764)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
