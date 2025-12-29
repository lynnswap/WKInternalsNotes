# ``WKInternalsNotes/WKFullScreenWindowController/didExitPictureInPicture()``

PiP 退出後の復帰条件を評価し、必要ならフルスクリーン復帰を試みる。

## Objective-C Declaration
```objective-c
- (void)didExitPictureInPicture;
```

## Discussion
`_shouldReturnToFullscreenFromPictureInPicture` が有効で `returningToStandbyInterface()` が standby への復帰中なら、フルスクリーン状態に応じて `preparedToReturnToStandby` を通知するか `requestRestoreFullScreen` を発行する。退出中の場合は `_enterRequested` を立てて後続で復帰させる。条件に合わない場合は `_enterFullscreenNeedsExitPictureInPicture` をクリアする。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1610`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1610)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
