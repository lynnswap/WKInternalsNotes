# ``WKInternalsNotes/WKFullScreenWindowController/enterFullScreen(_:)``

フルスクリーン開始要求を受け、必要な事前通知の後に遷移準備を開始する。

## Objective-C Declaration
```objective-c
- (void)enterFullScreen:(CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
GPU プロセスが存在する場合はスナップショット通知を発行した後、`_continueEnteringFullscreenAfterPostingNotification` に進む。GPU プロセスが未作成なら `completionHandler(false)` で終了する。準備処理では状態を `WaitingToEnterFullScreen` にし、WebView のスナップショット取得やプレースホルダー差し替え、リサイズ/スクロールイベントの抑制を行う。

## References
- [`WKFullScreenWindowController.mm#L437`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L437)
- [`WKFullScreenWindowController.mm#L369`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L369)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
