# ``WKInternalsNotes/WKFullScreenWindowController/didCleanupFullscreen()``

LINEAR_MEDIA_PLAYER の後処理で UI を再表示・再設定する。

## Objective-C Declaration
```objective-c
- (void)didCleanupFullscreen;
```

## Discussion
`ENABLE(LINEAR_MEDIA_PLAYER)` が有効でフルスクリーン中の場合に、`WKFullScreenViewController` の `showUI` と `configureEnvironmentPickerOrFullscreenVideoButtonView` を呼び、UI を再構成する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L2261`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2261)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
