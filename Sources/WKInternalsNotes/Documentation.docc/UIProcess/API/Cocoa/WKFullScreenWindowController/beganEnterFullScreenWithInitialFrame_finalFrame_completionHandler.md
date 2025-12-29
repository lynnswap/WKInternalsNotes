# ``WKInternalsNotes/WKFullScreenWindowController/beganEnterFullScreenWithInitialFrame(_:finalFrame:completionHandler:)``

フルスクリーン開始時に初期/最終フレームを保持し、状態遷移と表示準備を行う。

## Objective-C Declaration
```objective-c
- (void)beganEnterFullScreenWithInitialFrame:(CGRect)initialFrame finalFrame:(CGRect)finalFrame completionHandler:(CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
mac 版は `WaitingToEnterFullScreen` のときだけ状態を `EnteringFullScreen` に遷移し、初期/最終フレームを保存してアニメーションを「停止速度」で仕込み、フルスクリーンウィンドウを表示して `enterFullScreenMode:` を開始する。iOS 版はサイズの正規化とフレームの安全化を行ったうえで WebView を一時的に外し、フルスクリーン用 `UIViewController` を提示して完了時に `InFullScreen` へ遷移し、`completionHandler` を実行する。

## References
- [`WKFullScreenWindowController.mm#L456`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L456)
- [`WKFullScreenWindowControllerIOS.mm#L1211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1211)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
