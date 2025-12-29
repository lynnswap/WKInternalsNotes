# ``WKInternalsNotes/WKFullScreenViewController/configureEnvironmentPickerOrFullscreenVideoButtonView()``

環境ピッカーまたはフルスクリーン動画ボタンの表示を構成する。

## Objective-C Declaration
```objective-c
- (void)configureEnvironmentPickerOrFullscreenVideoButtonView;
```

## Discussion
`ENABLE(LINEAR_MEDIA_PLAYER)` のときのみ動作。設定や `PlaybackSessionModel` の対応状況に応じて、環境ピッカーやフルスクリーン動画ボタンを追加/削除し、delegate に `bestVideoPresentationInterfaceDidChange` を通知する。

## References
- [`WKFullScreenViewController.mm#L483`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L483)
- [`WKFullScreenViewController.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
