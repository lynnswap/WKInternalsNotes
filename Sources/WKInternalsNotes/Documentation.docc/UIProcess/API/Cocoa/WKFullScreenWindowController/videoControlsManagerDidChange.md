# ``WKInternalsNotes/WKFullScreenWindowController/videoControlsManagerDidChange()``

動画コントロールの更新をフルスクリーン UI に反映する。

## Objective-C Declaration
```objective-c
- (void)videoControlsManagerDidChange;
```

## Discussion
mac 版は空実装。iOS 版は `WKFullScreenViewController` が存在する場合に `videoControlsManagerDidChange` を転送する。

## References
- [`WKFullScreenWindowController.mm#L822`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L822)
- [`WKFullScreenWindowControllerIOS.mm#L1576`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1576)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
