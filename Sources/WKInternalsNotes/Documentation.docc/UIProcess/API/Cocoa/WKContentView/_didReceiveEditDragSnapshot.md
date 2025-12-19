# ``WKInternalsNotes/WKContentView/_didReceiveEditDragSnapshot(_:)``

編集ドラッグのスナップショット受信後の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didReceiveEditDragSnapshot:(RefPtr<WebCore::TextIndicator>&&)textIndicator;
```

## Discussion
受信待ちフラグを下げ、遅延ドロッププレビューの配信とドラッグ状態のクリーンアップを行う。待機していた処理があれば実行する。

## References
- [`WKContentViewInteraction.h#L899`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L899)
- [`WKContentViewInteraction.mm#L10815`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10815)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
