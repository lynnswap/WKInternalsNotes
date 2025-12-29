# ``WKInternalsNotes/WKFullScreenWindowController/videosInElementFullscreenChanged()``

要素フルスクリーン中の動画数変化をフルスクリーン UI に伝える。

## Objective-C Declaration
```objective-c
- (void)videosInElementFullscreenChanged;
```

## Discussion
`WKFullScreenViewController` が存在する場合に `videosInElementFullscreenChanged` を転送する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1582`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1582)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
