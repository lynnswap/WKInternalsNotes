# ``WKInternalsNotes/WKFullScreenViewController/hideUI()``

フルスクリーン UI を非表示にする。

## Objective-C Declaration
```objective-c
- (void)hideUI;
```

## Discussion
予約済みの `hideUI` をキャンセルし、メニュー表示中やシステムクローム操作中（visionOS）なら何もしない。アニメーション内で delegate の `hideUI` を呼び、スタックビューをフェードアウトし、ステータスバー/ホームインジケータを非表示にする。

## References
- [`WKFullScreenViewController.mm#L319`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L319)
- [`WKFullScreenViewController.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L59)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
