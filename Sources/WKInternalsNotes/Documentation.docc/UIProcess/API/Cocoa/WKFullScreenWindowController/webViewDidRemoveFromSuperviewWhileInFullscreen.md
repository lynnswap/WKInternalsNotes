# ``WKInternalsNotes/WKFullScreenWindowController/webViewDidRemoveFromSuperviewWhileInFullscreen()``

フルスクリーン中に WebView が外された場合の異常系処理を行う。

## Objective-C Declaration
```objective-c
- (void)webViewDidRemoveFromSuperviewWhileInFullscreen;
```

## Discussion
`InFullScreen` かつ WebView のウィンドウがフルスクリーン用ウィンドウと異なる場合に `_exitFullscreenImmediately` を呼び、強制的に終了する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1569`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1569)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
