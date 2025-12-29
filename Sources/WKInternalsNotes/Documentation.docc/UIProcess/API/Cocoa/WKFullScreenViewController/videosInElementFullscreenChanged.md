# ``WKInternalsNotes/WKFullScreenViewController/videosInElementFullscreenChanged()``

要素フルスクリーン内の動画状態変化を通知する。

## Objective-C Declaration
```objective-c
- (void)videosInElementFullscreenChanged;
```

## Discussion
`ENABLE(LINEAR_MEDIA_PLAYER)` の場合、`viewDidAppear` 後に `configureEnvironmentPickerOrFullscreenVideoButtonView` を呼んで UI を再構成する。

## References
- [`WKFullScreenViewController.mm#L434`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L434)
- [`WKFullScreenViewController.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
