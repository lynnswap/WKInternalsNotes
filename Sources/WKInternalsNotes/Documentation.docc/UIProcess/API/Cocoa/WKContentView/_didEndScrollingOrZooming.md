# ``WKInternalsNotes/WKContentView/_didEndScrollingOrZooming()``

スクロール/ズーム終了時の内部処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didEndScrollingOrZooming;
```

## Discussion
必要であれば `_textInteractionWrapper` に終了通知を送り、`WebPageProxy` のスクロール/ズーム状態を解除する。パン抑制フラグをリセットし、Pepper UI Core 環境ではフォーカス移動ナビゲーションを再開する。

## References
- [`WKContentViewInteraction.h#L825`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L825)
- [`WKContentViewInteraction.mm#L4177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4177)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
