# ``WKInternalsNotes/WKContentView/updateSelection()``

現在の選択操作状態に応じて選択を更新する。

## Objective-C Declaration
```objective-c
- (void)updateSelection;
```

## Discussion
`SelectionInteractionType` に応じてタッチ選択または範囲選択の更新処理に分岐する。

## References
- [`WKContentViewInteraction.h#L777`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L777)
- [`WKContentViewInteraction.mm#L5446`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5446)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
