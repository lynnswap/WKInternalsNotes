# ``WKInternalsNotes/WKFullScreenViewController/showUI()``

フルスクリーン UI を表示する。

## Objective-C Declaration
```objective-c
- (void)showUI;
```

## Discussion
予約済みの `hideUI` をキャンセルし、再生中なら `autoHideDelay` で `hideUI` を再予約する。アニメーション内で delegate の `showUI` を呼び、スタックビュー表示・ステータスバー/ホームインジケータ表示・トップ制約更新を行う。

## References
- [`WKFullScreenViewController.mm#L293`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L293)
- [`WKFullScreenViewController.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
