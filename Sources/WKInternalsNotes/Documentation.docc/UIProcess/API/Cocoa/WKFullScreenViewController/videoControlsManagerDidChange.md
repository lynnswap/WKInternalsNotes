# ``WKInternalsNotes/WKFullScreenViewController/videoControlsManagerDidChange()``

ビデオ操作 UI の状態変化に合わせてフルスクリーン UI を更新する。

## Objective-C Declaration
```objective-c
- (void)videoControlsManagerDidChange;
```

## Discussion
再生セッションを取得して `playing` を更新し、PiP の有効性/対応状況に応じてボタン表示を切り替える。`VIDEO_USES_ELEMENT_FULLSCREEN` や visionOS の設定に応じて追加ボタンの表示も更新する。

## References
- [`WKFullScreenViewController.mm#L401`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L401)
- [`WKFullScreenViewController.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
