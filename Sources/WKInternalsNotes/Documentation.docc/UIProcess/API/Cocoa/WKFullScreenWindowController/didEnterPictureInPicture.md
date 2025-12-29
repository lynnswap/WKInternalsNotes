# ``WKInternalsNotes/WKFullScreenWindowController/didEnterPictureInPicture()``

PiP への移行を検知し、必要ならフルスクリーン退出を要求する。

## Objective-C Declaration
```objective-c
- (void)didEnterPictureInPicture;
```

## Discussion
`_blocksReturnToFullscreenFromPictureInPicture` を考慮して `shouldReturnToFullscreen` を更新し、現在 `InFullScreen` であれば `requestExitFullScreen` を呼び出す。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1601`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1601)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
