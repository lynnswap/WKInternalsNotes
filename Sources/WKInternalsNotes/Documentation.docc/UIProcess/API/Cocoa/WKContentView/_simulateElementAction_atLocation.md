# ``WKInternalsNotes/WKContentView/_simulateElementAction(_:atLocation:)``

指定位置の要素アクションを実行する。

## Objective-C Declaration
```objective-c
- (void)_simulateElementAction:(_WKElementActionType)actionType atLocation:(CGPoint)location;
```

## Discussion
最新のレイヤーツリートランザクションIDを保持し、位置情報更新後に `_WKActivatedElementInfo` と `_WKElementAction` を構築して実行する。

## References
- [`WKContentViewInteraction.h#L1030`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1030)
- [`WKContentViewInteraction.mm#L14474`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14474)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
