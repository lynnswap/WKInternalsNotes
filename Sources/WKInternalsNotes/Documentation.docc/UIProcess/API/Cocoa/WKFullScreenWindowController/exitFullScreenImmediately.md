# ``WKInternalsNotes/WKFullScreenWindowController/exitFullScreenImmediately()``

フルスクリーン状態を即時終了し、通常の退出完了処理を強制的に走らせる。

## Objective-C Declaration
```objective-c
- (void)exitFullScreenImmediately;
```

## Discussion
`NotInFullScreen` なら何もしない。`WebFullScreenManagerProxy` に退出を要求し、退出警告を非表示にしたうえで状態を `ExitingFullScreen` に切り替え、`finishedExitFullScreenAnimationAndExitImmediately:YES` を呼んで終了処理を即時実行する。

## References
- [`WKFullScreenWindowController.mm#L614`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L614)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
