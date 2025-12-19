# ``WKInternalsNotes/WKContentView/animatingDragCancel``

ドラッグキャンセルのアニメーション中かどうか。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isAnimatingDragCancel) BOOL animatingDragCancel;
```

## Default Value
NO（キャンセルアニメーション中のみYES）。

## Discussion
`dragInteraction:willAnimateCancelWithAnimator:` 開始時に `YES` となり、完了後に `NO` へ戻る。

## References
- [`WKContentViewInteraction.h#L1069`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1069)
- [`WKContentViewInteraction.mm#L11297`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11297)
- [`WKContentViewInteraction.mm#L14445`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14445)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
