# ``WKInternalsNotes/WKWebView/_playingAudio``

`_playingAudio` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isPlayingAudio) BOOL _playingAudio WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isPlayingAudio`。

## References
- [`WKWebViewPrivate.h#L221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L221)
- [`WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
