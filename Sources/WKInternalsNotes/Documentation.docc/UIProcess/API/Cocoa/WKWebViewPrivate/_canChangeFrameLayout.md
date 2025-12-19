# ``WKInternalsNotes/WKWebView/_canChangeFrameLayout(_:)``

`_canChangeFrameLayout` の状態を返す。

## Objective-C Declaration
```objective-c
- (BOOL)_canChangeFrameLayout:(_WKFrameHandle *)frameHandle WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L877`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L877)
- [`API/mac/WKWebViewMac.mm#L1889`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1889)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
