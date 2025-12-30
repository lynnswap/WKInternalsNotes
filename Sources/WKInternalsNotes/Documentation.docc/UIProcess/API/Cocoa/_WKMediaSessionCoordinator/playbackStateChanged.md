# ``WKInternalsNotes/_WKMediaSessionCoordinator/playbackStateChanged(_:)``

MediaSession の playback state をクライアントに伝える。

## Objective-C Declaration
```objective-c
- (void)playbackStateChanged:(_WKMediaSessionPlaybackState)state;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` は enum の一致を `static_assert` で確認した上で `_WKMediaSessionPlaybackState` にキャストして渡す。

## References
- [`WKWebViewPrivateForTesting.h#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L229)
- [`WKWebViewTesting.mm#L899`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L899)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
