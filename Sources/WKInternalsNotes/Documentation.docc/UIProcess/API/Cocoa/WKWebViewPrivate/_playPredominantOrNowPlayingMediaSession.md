# ``WKInternalsNotes/WKWebView/_playPredominantOrNowPlayingMediaSession(_:)``

`_playPredominantOrNowPlayingMediaSession` を実行する。

## Objective-C Declaration
```objective-c
- (void)_playPredominantOrNowPlayingMediaSession:(void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L621`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L621)
- [`WKWebView.mm#L6300`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6300)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
