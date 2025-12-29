# ``WKInternalsNotes/WKFullScreenWindowController/exitFullScreen(_:)``

フルスクリーン終了要求を受け、状態更新と退出準備を行う。

## Objective-C Declaration
```objective-c
- (void)exitFullScreen:(CompletionHandler<void()>&&)completionHandler;
```

## Discussion
mac 版は「まだ入場中」の場合に completion を保持して後で実行し、フルスクリーン中なら `WaitingToExitFullScreen` に遷移して描画更新を抑制し、`WebFullScreenManagerProxy` にアニメーション中であることを通知する。iOS 版は watchdog を止め、状態に応じて `_exitRequested` を立てるか、QuickLook の場合はプレビューを閉じて終了処理に進む。通常は `_beginAnimatedFullScreenExit` を呼び、`WaitingToExitFullScreen` にしてアニメーション開始と watchdog をセットする。

## References
- [`WKFullScreenWindowController.mm#L575`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L575)
- [`WKFullScreenWindowControllerIOS.mm#L1367`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1367)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
