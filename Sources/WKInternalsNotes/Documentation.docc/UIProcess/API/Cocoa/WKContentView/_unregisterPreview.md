# ``WKInternalsNotes/WKContentView/_unregisterPreview()``

リンクプレビュー用の登録を解除する。

## Objective-C Declaration
```objective-c
- (void)_unregisterPreview;
```

## Discussion
UIContextMenu を使う構成では何もしない。レガシー経路では `UIPreviewItemController` の delegate を外し、ジェスチャ参照とコントローラを解放する。

## References
- [`WKContentViewInteraction.h#L1085`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1085)
- [`WKContentViewInteraction.mm#L14770`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14770)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
