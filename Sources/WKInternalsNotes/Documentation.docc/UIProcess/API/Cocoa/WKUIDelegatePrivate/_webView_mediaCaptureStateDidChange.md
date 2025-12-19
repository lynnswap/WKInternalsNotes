# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:mediaCaptureStateDidChange:)``

メディアキャプチャ状態の変化を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView mediaCaptureStateDidChange:(_WKMediaCaptureStateDeprecated)state WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
UIClient が `mediaCaptureState` の KVO を更新した後、`WebCore::MediaProducerMediaStateFlags` を `_WKMediaCaptureStateDeprecated` に変換して delegate へ渡す。

## References
- [`WKUIDelegatePrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L158)
- [`UIDelegate.mm#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L178)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
