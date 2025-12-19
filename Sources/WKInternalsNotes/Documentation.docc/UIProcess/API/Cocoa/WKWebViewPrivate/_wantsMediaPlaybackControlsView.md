# ``WKInternalsNotes/WKWebView/_wantsMediaPlaybackControlsView``

`_wantsMediaPlaybackControlsView` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setWantsMediaPlaybackControlsView:) BOOL _wantsMediaPlaybackControlsView WK_API_AVAILABLE(macos(10.12.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setWantsMediaPlaybackControlsView:`。

## References
- [`WKWebViewPrivate.h#L908`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L908)
- [`WKWebViewMac.mm#L1995`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1995)
- [`WKWebViewMac.mm#L1995`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1995)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
