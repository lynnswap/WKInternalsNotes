# ``WKInternalsNotes/WKFullScreenWindowController/didEnterVideoFullscreen()``

visionOS で動画フルスクリーン開始時にステージの暗さ設定を解除する。

## Objective-C Declaration
```objective-c
- (void)didEnterVideoFullscreen;
```

## Discussion
`PLATFORM(VISION)` かつ `isFullScreen` のとき、`UIApplication.sharedApplication.mrui_activeStage.preferredDarkness` を `MRUIDarknessPreferenceUnspecified` に戻す。それ以外の環境では処理しない。

## References
- [`WKFullScreenWindowControllerIOS.mm#L992`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L992)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
