# ``WKInternalsNotes/WKFullScreenViewControllerDelegate/requestExitFullScreen()``

フルスクリーン終了要求を委譲する。

## Objective-C Declaration
```objective-c
- (void)requestExitFullScreen;
```

## Discussion
`WKFullScreenWindowControllerIOS` の実装では状態に応じてフラグを立てるか、`FullscreenManager` に終了要求を送る。マネージャが不在の場合は即時終了を試みる。

## References
- [`WKFullScreenViewController.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L37)
- [`WKFullScreenWindowControllerIOS.mm#L1347`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1347)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
