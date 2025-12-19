# ``WKInternalsNotes/WKContentView/_canStartNavigationSwipeAtLastInteractionLocation``

最後の操作位置でナビゲーションスワイプが開始可能かを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _canStartNavigationSwipeAtLastInteractionLocation;
```

## Default Value
ヒットビューが無い場合は `YES`。スクロール中のビューがあれば `NO`。

## Discussion
最後にタッチした位置のビュー階層でスクロール中やパンジェスチャ実行中のスクロールビューがあれば `NO`。問題がなければタッチアクションが `Auto`/`PanX`/`Manipulation` を含む場合のみ `YES` を返す。

## References
- [`WKContentViewInteraction.h#L945`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L945)
- [`WKContentViewInteraction.mm#L14314`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14314)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
