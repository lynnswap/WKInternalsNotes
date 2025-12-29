# ``WKInternalsNotes/WKFullScreenWindowController/beganExitFullScreenWithInitialFrame(_:finalFrame:completionHandler:)``

フルスクリーン終了開始時に初期/最終フレームを記録し、終了遷移を開始する。

## Objective-C Declaration
```objective-c
- (void)beganExitFullScreenWithInitialFrame:(CGRect)initialFrame finalFrame:(CGRect)finalFrame completionHandler:(CompletionHandler<void()>&&)completionHandler;
```

## Discussion
mac 版は `WaitingToExitFullScreen` のときだけ `ExitingFullScreen` に遷移して完了ハンドラを保持し、必要なら即時終了処理に進んだうえで `exitFullScreenMode:` を呼ぶ。iOS 版はフレームの正規化と安全化を行い、表示更新を抑制しつつフルスクリーン VC を dismiss する（ジェスチャーによるインタラクティブ退出中はその完了を優先する）。

## References
- [`WKFullScreenWindowController.mm#L637`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L637)
- [`WKFullScreenWindowControllerIOS.mm#L1423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
