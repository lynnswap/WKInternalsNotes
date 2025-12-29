# ``WKInternalsNotes/_WKFullscreenDelegate/_webView(_:didFullscreenImageWithQuickLook:)``

QuickLook で画像をフルスクリーン表示したことを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFullscreenImageWithQuickLook:(CGSize)imageDimensions;
```

## Discussion
`FullscreenClient::didEnterFullscreen` で QuickLook を使用している場合に呼び出され、画像のサイズを渡す。

## References
- [`_WKFullscreenDelegate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L44)
- [`FullscreenClient.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L102)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
