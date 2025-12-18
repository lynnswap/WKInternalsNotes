# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:hasVideoInPictureInPictureDidChange:)``

ピクチャインピクチャの動画有無の変化を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView hasVideoInPictureInPictureDidChange:(BOOL)hasVideoInPictureInPicture WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
VideoPresentationManagerProxy からの通知を UIClient が受け取り、PiP で動画が存在するかを delegate に伝える。

## References
- [`WKUIDelegatePrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L158)
- [`UIDelegate.mm#L1902`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1902)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
