# ``WKInternalsNotes/WKContentView/didReceiveInteractiveModelElement(_:)``

インタラクティブモデル要素の受信結果を反映する。

## Objective-C Declaration
```objective-c
- (void)didReceiveInteractiveModelElement:(std::optional<WebCore::NodeIdentifier>)nodeID;
```

## Discussion
ステージモードセッションが無いか準備中でなければ何もしない。準備中の場合は `nodeID` を保存し、値があれば準備完了として `isPreparingForInteraction` を false にする。

## References
- [`WKContentViewInteraction.h#L907`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L907)
- [`WKContentViewInteraction.mm#L11575`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11575)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
