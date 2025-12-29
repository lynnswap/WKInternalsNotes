# ``WKInternalsNotes/WKFullScreenViewController/invalidate()``

フルスクリーン表示を無効化し、関連リソースを解放する。

## Objective-C Declaration
```objective-c
- (void)invalidate;
```

## Discussion
`_valid` が `NO` の場合は何もしない。必要に応じて再生を停止し、予約済みの `hideUI`/`hideBanner` をキャンセル、通知解除、PlaybackSession のクライアント解除を行った上で delegate に無効化を通知する。

## References
- [`WKFullScreenViewController.mm#L235`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L235)
- [`WKFullScreenViewController.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
