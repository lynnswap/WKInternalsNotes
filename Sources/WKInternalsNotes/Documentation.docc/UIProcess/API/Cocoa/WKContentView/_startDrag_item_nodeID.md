# ``WKInternalsNotes/WKContentView/_startDrag(_:item:nodeID:)``

ドラッグ開始に向けてアイテムを準備する。

## Objective-C Declaration
```objective-c
- (void)_startDrag:(RetainPtr<CGImageRef>)image item:(const WebCore::DragItem&)item nodeID:(std::optional<WebCore::NodeIdentifier>)nodeID;
```

## Discussion
モデルプロセス対応時は nodeID を保持し、モデル用のドラッグプレビューが取得できればそれを使ってステージングする。添付ファイルのドラッグでは準備処理を行い、最終的に `CGImage` から `UIImage` を作成してドラッグアイテムをステージングする。

## References
- [`WKContentViewInteraction.h#L897`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L897)
- [`WKContentViewInteraction.mm#L10604`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10604)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
