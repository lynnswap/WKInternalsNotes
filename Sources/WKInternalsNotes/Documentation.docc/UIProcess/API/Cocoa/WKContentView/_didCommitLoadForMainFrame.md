# ``WKInternalsNotes/WKContentView/_didCommitLoadForMainFrame()``

メインフレームの commit 時に状態をリセットする。

## Objective-C Declaration
```objective-c
- (void)_didCommitLoadForMainFrame;
```

## Discussion
スクロール/入力/選択状態をリセットし、各種プレビューコンテナを削除して WebView 側へ通知する。

## References
- [`WKContentViewInteraction.h#L926`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L926)
- [`WKContentViewInteraction.mm#L6142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6142)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
