# ``WKInternalsNotes/WKWebView/_enterExternalPlaybackForNowPlayingMediaSessionWithEnterCompletionHandler(_:exitCompletionHandler:)``

`_enterExternalPlaybackForNowPlayingMediaSessionWithEnterCompletionHandler` を実行する。

## Objective-C Declaration
```objective-c
- (void)_enterExternalPlaybackForNowPlayingMediaSessionWithEnterCompletionHandler:(void (^)(UIViewController *nowPlayingViewController, NSError *error))enterHandler exitCompletionHandler:(void (^)(NSError *error))exitHandler WK_API_AVAILABLE(visionos(26.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L799`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L799)
- [`WKWebViewIOS.mm#L5287`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5287)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
