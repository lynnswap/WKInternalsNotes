# ``WKInternalsNotes/WKFullScreenWindowController/_startExitFullScreenAnimationWithDuration(_:)``

フルスクリーン終了時のズーム/マスク/フェードのアニメーションを開始し、必要なら退出要求を送る。

## Objective-C Declaration
```objective-c
- (void)_startExitFullScreenAnimationWithDuration:(NSTimeInterval)duration;
```

## Discussion
まだフルスクリーン中と判断されている場合は `WebFullScreenManagerProxy` に退出を要求し、`exitFullScreen:` を呼んで状態を `ExitingFullScreen` に更新する。その後、`_clipView` のレイヤにズーム、マスク、背景フェードを追加し、コンテンツビューを可視に戻して表示更新を再開する。

## References
- [`WKFullScreenWindowController.mm#L1054`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L1054)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
